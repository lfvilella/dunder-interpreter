# della-compiler
Compiler using ANTLR + LLVM

# Dev

## .vscode folder

launch.json
```json
{
    "version": "2.0.0",
    "configurations": [
        {
            "name": "antlr4-DecisionGrammar",
            "type": "antlr-debug",
            "request": "launch",
            "input": "path/test.txt",
            "grammar": "path/tinyc.g4",
            "startRule": "prog",
            "printParseTree": true,
            "visualParseTree": true
        }
    ]
}
```
