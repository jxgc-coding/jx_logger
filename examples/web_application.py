#!/usr/bin/env python3
"""
Web application example for JX Logger.

This example demonstrates using JX Logger in a web application context
with request tracking, user context, and structured logging.
"""

import uuid
import time
from typing import Dict, Any
from jx_logger import get_logger, LogContext, with_context

class MockRequest:
    """Mock request object for demonstration."""
    def __init__(self, path: str, method: str = "GET", user_id: str = None):
        self.path = path
        self.method = method
        self.user_id = user_id
        self.request_id = str(uuid.uuid4())

class WebApp:
    """Mock web application with integrated logging."""
    
    def __init__(self):
        self.logger = get_logger(
            name="webapp",
            log_format="rich",
            level="INFO",
            console_output=True,
            mask_sensitive_data=True
        )
        self.request_count = 0
    
    def middleware_logging(self, request: MockRequest):
        """Middleware to set up request context."""
        context = LogContext(
            request_id=request.request_id,
            user_id=request.user_id,
            component="web",
            operation=f"{request.method} {request.path}"
        )
        self.logger.set_context(context)
        
        self.request_count += 1
        self.logger.info(f"Incoming request", extra={
            "method": request.method,
            "path": request.path,
            "request_count": self.request_count
        })
    
    @with_context(component="auth")
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate user with logging."""
        self.logger.info(f"Authentication attempt for user: {username}")
        
        # Simulate authentication logic
        time.sleep(0.1)
        
        if username == "admin" and password == "secret":
            self.logger.success(f"User {username} authenticated successfully")
            return True
        else:
            self.logger.warning(f"Authentication failed for user: {username}")
            return False
    
    @with_context(component="database")
    def get_user_data(self, user_id: str) -> Dict[str, Any]:
        """Get user data with logging."""
        self.logger.debug(f"Fetching user data for user_id: {user_id}")
        
        # Simulate database query
        time.sleep(0.05)
        
        user_data = {
            "user_id": user_id,
            "username": "john_doe",
            "email": "john@example.com",
            "password_hash": "hashed_password_123",  # Will be masked
            "api_token": "token_abc123"  # Will be masked
        }
        
        self.logger.success("User data retrieved successfully")
        return user_data
    
    @with_context(component="business_logic")
    def process_order(self, order_data: Dict[str, Any]):
        """Process order with comprehensive logging."""
        order_id = order_data.get("order_id")
        amount = order_data.get("amount")
        
        self.logger.info(f"Processing order {order_id}", extra={
            "order_id": order_id,
            "amount": amount,
            "items_count": len(order_data.get("items", []))
        })
        
        try:
            # Simulate order processing
            time.sleep(0.2)
            
            if amount > 1000:
                self.logger.warning(f"High-value order detected: ${amount}")
            
            # Simulate payment processing
            self.logger.debug("Processing payment")
            time.sleep(0.1)
            
            self.logger.success(f"Order {order_id} processed successfully", extra={
                "processing_time": "0.3s",
                "payment_status": "completed"
            })
            
        except Exception as e:
            self.logger.error(f"Order processing failed for {order_id}: {str(e)}")
            raise
    
    def handle_request(self, request: MockRequest):
        """Handle a complete request with logging."""
        start_time = time.time()
        
        try:
            # Set up request context
            self.middleware_logging(request)
            
            if request.path == "/login":
                # Simulate login
                success = self.authenticate_user("admin", "secret")
                if success:
                    request.user_id = "user_123"
                    return {"status": "success", "message": "Logged in"}
                else:
                    return {"status": "error", "message": "Authentication failed"}
            
            elif request.path == "/profile":
                # Simulate profile request
                if not request.user_id:
                    self.logger.warning("Unauthorized profile access attempt")
                    return {"status": "error", "message": "Unauthorized"}
                
                user_data = self.get_user_data(request.user_id)
                return {"status": "success", "data": user_data}
            
            elif request.path == "/order":
                # Simulate order processing
                order_data = {
                    "order_id": "ord_456",
                    "amount": 1250.00,
                    "items": ["item1", "item2"]
                }
                self.process_order(order_data)
                return {"status": "success", "message": "Order processed"}
            
            else:
                self.logger.warning(f"Unknown endpoint: {request.path}")
                return {"status": "error", "message": "Not found"}
        
        except Exception as e:
            self.logger.exception(f"Request failed: {str(e)}")
            return {"status": "error", "message": "Internal server error"}
        
        finally:
            # Log request completion
            duration = time.time() - start_time
            self.logger.info(f"Request completed", extra={
                "duration": f"{duration:.3f}s",
                "status": "completed"
            })

def main():
    """Demonstrate web application logging."""
    
    print("🚀 JX Logger - Web Application Example")
    print("=" * 50)
    
    app = WebApp()
    
    # Simulate various requests
    requests = [
        MockRequest("/login", "POST"),
        MockRequest("/profile", "GET", "user_123"),
        MockRequest("/order", "POST", "user_123"),
        MockRequest("/unknown", "GET"),
    ]
    
    for i, req in enumerate(requests, 1):
        print(f"\n{i}. Processing {req.method} {req.path}")
        response = app.handle_request(req)
        print(f"   Response: {response['status']}")
    
    # Show performance stats
    print("\n📊 Performance Statistics:")
    stats = app.logger.get_performance_stats()
    if stats:
        print(f"   Total logs: {stats['total_logs']}")
        print(f"   Logs per second: {stats['logs_per_second']:.2f}")
        for level, count in stats['log_counts_by_level'].items():
            print(f"   {level}: {count}")
    
    print("\n✅ Web application example completed!")

if __name__ == "__main__":
    main()