# DeepSeek Engineer 🐋

## Overview

DeepSeek Engineer is a powerful AI-powered coding assistant that provides an interactive terminal interface for seamless code development. It integrates with DeepSeek's advanced reasoning models to offer intelligent file operations, code analysis, and development assistance through natural conversation and function calling.

## 🚀 Latest Update: Function Calling Architecture

**Version 2.0** introduces a revolutionary upgrade from structured JSON output to native function calling, providing:
- **Natural conversations** with the AI without rigid response formats
- **Automatic file operations** through intelligent function calls
- **Real-time reasoning visibility** with Chain of Thought (CoT) capabilities
- **Enhanced reliability** and better error handling

## Key Features

### 🧠 **AI Capabilities**
- **Elite Software Engineering**: Decades of experience across all programming domains
- **Chain of Thought Reasoning**: Visible thought process before providing solutions
- **Code Analysis & Discussion**: Expert-level insights and optimization suggestions
- **Intelligent Problem Solving**: Automatic file reading and context understanding

### 🛠️ **Function Calling Tools**
The AI can automatically execute these operations:

#### `read_file(file_path: str)`
- Read single file content with automatic path normalization
- Built-in error handling for missing or inaccessible files

#### `read_multiple_files(file_paths: List[str])`
- Batch read multiple files efficiently
- Formatted output with clear file separators

#### `create_file(file_path: str, content: str)`
- Create new files or overwrite existing ones
- Automatic directory creation and safety checks
- No manual confirmation required

#### `create_multiple_files(files: List[Dict])`
- Create multiple files in a single operation
- Perfect for scaffolding projects or creating related files

#### `edit_file(file_path: str, original_snippet: str, new_snippet: str)`
- Precise snippet-based file editing
- Visual diff preview with user confirmation
- Safe replacement with exact matching

### 📁 **Manual File Operations**
- **`/add path/to/file`** - Include single file in conversation context
- **`/add path/to/folder`** - Include entire directory (with smart filtering)
- **Automatic context management** - Files remain available throughout the session

### 🎨 **Rich Terminal Interface**
- **Color-coded feedback** (green for success, red for errors, yellow for warnings)
- **Real-time streaming** with visible reasoning process
- **Structured tables** for diff previews
- **Progress indicators** for long operations

### 🛡️ **Security & Safety**
- **Path normalization** and validation
- **Directory traversal protection**
- **File size limits** (5MB per file)
- **Binary file detection** and exclusion
- **User confirmation** for destructive operations

## Getting Started

### Prerequisites
1. **DeepSeek API Key**: Get your API key from [DeepSeek Platform](https://platform.deepseek.com)
2. **Python 3.11+**: Required for optimal performance

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd deepseek-engineer
   ```

2. **Set up environment**:
   ```bash
   # Create .env file
   echo "DEEPSEEK_API_KEY=your_api_key_here" > .env
   ```

3. **Install dependencies** (choose one method):

   #### Using uv (recommended - faster)
   ```bash
   uv venv
   uv run r1.py
   ```

   #### Using pip
   ```bash
   pip install -r requirements.txt
   python3 r1.py
   ```

### Usage Examples

#### **Natural Conversation with File Operations**
```
You> Can you read the main.py file and create a test file for it?

Thinking...
Reasoning: I need to first read the main.py file to understand its structure...

Assistant> I'll read the main.py file first to understand its structure.
→ read_file("main.py")
✓ Read file 'main.py'

Now I'll create comprehensive tests based on the code structure I found.
→ create_file("test_main.py", content="import unittest...")
✓ Created file 'test_main.py'

I've analyzed main.py and created comprehensive tests covering all the main functions...
```

#### **Code Analysis and Improvements**
```
You> /add src/

✓ Added folder 'src/' to conversation.
Added files: (15 files)
  src/utils.py
  src/models.py
  ...

You> Can you review this codebase and suggest improvements?

Thinking...
Reasoning: I'll analyze the codebase structure, looking for patterns, potential issues...

Assistant> I've reviewed your codebase and found several areas for improvement:

1. **Error Handling**: The utils.py file could benefit from more robust error handling...
→ edit_file("src/utils.py", original_snippet="def process_data(data):", new_snippet="def process_data(data):\n    if not data:\n        raise ValueError('Data cannot be empty')")

Would you like me to apply this improvement?
```

## Available Versions

### **r1.py (Recommended) - Function Calling + Reasoning**
- **Latest architecture** with function calling
- **Chain of Thought reasoning** visible in real-time
- **Natural conversation flow**
- **Automatic file operations**
- **Enhanced error handling**

```bash
python3 r1.py  # or uv run r1.py
```

### **main.py (Legacy) - Structured JSON Output**
- **Original version** with JSON-based responses
- **Manual confirmation** for all file operations
- **Structured output parsing**
- **Still functional** but less intuitive

```bash
python3 main.py  # or uv run main.py
```

## Advanced Features

### **Intelligent Context Management**
- **Automatic file detection** from user messages
- **Smart conversation cleanup** to prevent token overflow
- **File content preservation** across conversation history
- **Tool message integration** for complete operation tracking

### **Batch Operations**
```
You> Create a complete Flask API with models, routes, and tests

Assistant> I'll create a complete Flask API structure for you.
→ create_multiple_files([
    {"path": "app.py", "content": "from flask import Flask..."},
    {"path": "models.py", "content": "from sqlalchemy import..."},
    {"path": "routes.py", "content": "from flask import Blueprint..."},
    {"path": "test_api.py", "content": "import unittest..."}
])
```

### **Project Analysis**
```
You> /add .
You> Analyze this entire project and suggest a refactoring plan

Assistant> → read_multiple_files(["main.py", "r1.py", "requirements.txt"])
Based on my analysis of your project, here's a comprehensive refactoring plan...
```

## Technical Architecture

### **Function Call Execution Flow**
1. **User Input** → Natural language request
2. **AI Reasoning** → Visible thought process (CoT)
3. **Function Calls** → Automatic tool execution
4. **Real-time Feedback** → Operation status and results
5. **Follow-up Response** → AI processes results and responds

### **Streaming Architecture**
- **Triple-stream processing**: reasoning + content + tool_calls
- **Real-time tool execution** during streaming
- **Automatic follow-up** responses after tool completion
- **Error recovery** and graceful degradation

### **Security Model**
- **Path validation** with directory traversal prevention
- **File size limits** and binary detection
- **User confirmation** for destructive operations
- **Sandboxed execution** environment

## Migration from v1.0

If you're upgrading from the original JSON-based version:

### **What's New**
- ✅ Natural conversation instead of JSON responses
- ✅ Automatic file operations via function calls
- ✅ Real-time reasoning visibility
- ✅ Better error handling and recovery
- ✅ Enhanced streaming architecture

### **What's Preserved**
- ✅ `/add` command functionality
- ✅ Rich terminal interface
- ✅ File editing with diff preview
- ✅ Security and safety features
- ✅ DeepSeek reasoning model integration

### **Migration Steps**
1. Update to use `r1.py` instead of `main.py`
2. Enjoy more natural conversations
3. No changes needed to your workflow

## Contributing

This is an experimental project showcasing DeepSeek v3 API capabilities. Contributions are welcome!

### **Development Setup**
```bash
git clone <repository-url>
cd deepseek-engineer
uv venv
uv sync
```

### **Testing**
```bash
# Test import and basic functionality
python3 -c "import r1; print('✓ Import successful')"

# Test function calling tools
python3 -c "import r1; print(f'✓ {len(r1.tools)} tools available')"
```

## Troubleshooting

### **Common Issues**

**API Key Not Found**
```bash
# Make sure .env file exists with your API key
echo "DEEPSEEK_API_KEY=your_key_here" > .env
```

**Import Errors**
```bash
# Install dependencies
uv sync  # or pip install -r requirements.txt
```

**File Permission Errors**
- Ensure you have write permissions in the working directory
- Check file paths are correct and accessible

## License

This project is experimental and developed for testing DeepSeek v3 API capabilities.

---

> **Note**: This is an experimental project developed by Skirano to explore the capabilities of DeepSeek's v3 API with function calling and reasoning models. Use responsibly and enjoy the enhanced AI pair programming experience! 🚀

