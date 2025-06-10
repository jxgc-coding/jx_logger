# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added
- Initial release of JX Logger
- Rich console output with colorized log levels and emojis
- Custom log levels: SUCCESS (Level 25) and TRACE (Level 5)
- Asynchronous logging support with queue-based architecture
- Automatic sensitive data masking for passwords, tokens, etc.
- Structured JSON logging for machine-readable output
- Contextual logging with request IDs, user context, and correlation tracking
- Performance monitoring with built-in metrics
- Multiple output formats: JSON, Rich, Console, and Structured
- Drop-in replacement convenience functions for standard Python logging
- Comprehensive documentation and examples
- Type hints for better IDE support
- Thread-safe and async-safe context management

### Features
- 🎨 **Rich Console Output** - Beautiful, colorized logs
- ⚡ **Async Logging** - Non-blocking logging operations
- 🏗️ **Structured JSON** - Machine-readable log format
- 🔐 **Data Masking** - Automatic protection of sensitive information
- 📊 **Performance Monitoring** - Built-in metrics and statistics
- 🔍 **Contextual Information** - Rich context tracking
- 🎯 **Custom Log Levels** - SUCCESS and TRACE with visual indicators
- 🔄 **Multiple Formats** - Flexible output options
- 🎭 **Easy Integration** - Simple drop-in replacement

### Dependencies
- Python 3.8+
- Rich (optional, for colorized console output)
- typing-extensions (for Python < 3.10)

### Documentation
- Comprehensive README with usage examples
- API documentation in docstrings
- Example scripts for different use cases
- Type hints for better IDE support