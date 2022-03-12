# Development Doc

**Subtitles**

symbol | meaning
--- | ---
$ | cmd
\# | inside container

## ANTLR

    $ docker-compose exec java /bin/bash

Run **alias** commands commented on `java/Dockerfile`. We're working on to solve.

    # antlr4 Hello.g4 -o antlr -listener -visitor

*Note: If you get this error: `error(7):  cannot find or open file:`. Try to run a couple of times, should work, we're working on to fix it.*

The next steps is integrate both parts, see an example like on `c` folder.

## LLVM


    $ docker-compose exec clang /bin/bash
    # clang -emit-llvm -S hello.c -o hello.ll

Possible to execute the IR running the lli which directly execute the IR.

    # lli hello.ll

Create an executable binary we can pass the IR file to clang.

    # clang -x ir hello.ll -o hello.out
    # ./hello.out
