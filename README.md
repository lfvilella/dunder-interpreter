# dunder interpreter

*Note: This repo is just to education goals*

Implemented:
- C compiler using ANTLR + Clang + LLVM
- tinyC interpreter using ANTLR + Python

Wip:
- dunder cats language interpreted with Python

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
