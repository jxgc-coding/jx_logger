#!/usr/bin/env python3
"""
Async logging example for JX Logger.

This example demonstrates async logging capabilities and patterns.
"""

import asyncio
import time
from jx_logger import get_logger, LogFormat, LogContext

async def simulate_async_operation(logger, operation_name: str, duration: float):
    """Simulate an async operation with logging."""
    logger.info(f"Starting {operation_name}")
    
    # Simulate work
    await asyncio.sleep(duration)
    
    logger.success(f"Completed {operation_name} in {duration}s")

async def async_with_context(logger):
    """Demonstrate async logging with context."""
    context = LogContext(
        request_id="async_req_789",
        component="async_processor"
    )
    logger.set_context(context)
    
    await logger.ainfo("Async operation with context started")
    await asyncio.sleep(0.1)
    await logger.asuccess("Async operation with context completed")

async def main():
    """Demonstrate async logging patterns."""
    
    print("🚀 JX Logger - Async Logging Example")
    print("=" * 50)
    
    # Create async logger
    logger = get_logger(
        name="async-example",
        log_format=LogFormat.RICH,
        level="DEBUG",
        async_logging=True,
        console_output=True
    )
    
    print("\n1. Basic Async Logging:")
    await logger.ainfo("Async logger initialized")
    await logger.adebug("This is an async debug message")
    
    print("\n2. Concurrent Operations:")
    tasks = [
        simulate_async_operation(logger, "Database Query", 0.2),
        simulate_async_operation(logger, "API Call", 0.3),
        simulate_async_operation(logger, "File Processing", 0.1),
    ]
    
    start_time = time.time()
    await asyncio.gather(*tasks)
    total_time = time.time() - start_time
    
    logger.success(f"All operations completed in {total_time:.2f}s")
    
    print("\n3. Async with Context:")
    await async_with_context(logger)
    
    print("\n4. Error Handling:")
    try:
        # Simulate an error
        raise ValueError("Simulated async error")
    except ValueError as e:
        await logger.aerror(f"Caught exception: {str(e)}")
    
    # Give async handlers time to process
    await asyncio.sleep(0.1)
    
    print("\n✅ Async logging example completed!")

if __name__ == "__main__":
    asyncio.run(main())