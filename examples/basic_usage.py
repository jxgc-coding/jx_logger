#!/usr/bin/env python3
"""
Basic usage example for JX Logger.

This example demonstrates the core features and basic usage patterns.
"""

import time
from jx_logger import get_logger, LogFormat, LogContext

def main():
    """Demonstrate basic JX Logger usage."""
    
    print("🚀 JX Logger - Basic Usage Example")
    print("=" * 50)
    
    # Create a logger with Rich formatting
    logger = get_logger(
        name="basic-example",
        log_format=LogFormat.RICH,
        level="DEBUG",
        console_output=True
    )
    
    print("\n1. Basic Log Levels:")
    logger.trace("🔬 This is a trace message")
    logger.debug("🔍 This is a debug message")
    logger.info("ℹ️ This is an info message")
    logger.success("✅ This is a success message")
    logger.warning("⚠️ This is a warning message")
    logger.error("❌ This is an error message")
    logger.critical("🚨 This is a critical message")
    
    print("\n2. Contextual Logging:")
    context = LogContext(
        request_id="req_123",
        user_id="user_456",
        component="auth"
    )
    logger.set_context(context)
    logger.info("User authentication started")
    logger.success("User authenticated successfully")
    
    print("\n3. Extra Data:")
    logger.info("Processing user data", extra={
        "user_count": 1234,
        "processing_time": 0.5,
        "memory_usage": "85%"
    })
    
    print("\n4. Sensitive Data Masking:")
    logger.info("User login attempt", extra={
        "username": "john_doe",
        "password": "secret123",  # This will be automatically masked
        "api_key": "sk-1234567890"  # This will be automatically masked
    })
    
    print("\n5. Performance Stats:")
    if logger.enable_performance_monitoring:
        stats = logger.get_performance_stats()
        logger.info("Logger performance", extra={"stats": stats})
    
    print("\n✅ Basic usage example completed!")

if __name__ == "__main__":
    main()