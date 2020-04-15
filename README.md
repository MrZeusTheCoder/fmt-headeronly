> ¡WARNING YOU ARE ON THE MASTER BRANCH! ¡THIS MIRRORS (>WHEN UPDATED<) THE MASTER BRANCH OF {FMT}, WHICH MAY BE UNSTABLE!

---

# `fmt::format`, but header-only.

A striped version of fmt that only contains `fmt/format.h` and the files it depends on. It is header-only.
It does not contain all the features the compiled version does,

## Usage:

```C++
#include <fmt/format.h>
or
#include "path/to/fmt/include/fmt/format.h"
```

## UGH, you don't have the version I want... What do I do?

Make it yourself. All you have to do is clone [`{fmt}`](https://github.com/fmtlib/fmt), checkout to the branch/tag you want,, `python3 make_fmt_headeronly.py [path to the {fmt} directory]`, and then copy the files out of the newly generated `output` folder into your existing `include/fmt/` directory. 

:), simple.

<br>

### Disclaimers:

1. `{fmt}` has built-in functionality to be header only. My code simply forces this functionality into the *ON* position.
2. `{fmt}` requires all distributed modifications of its code to hold the same licence as it. This licence can be seen in the `LICENSE` file.

<br><br><br><br><br><br><br><br><br><br><br><br>
<h6><sub>Your welcome, counter, undefined, and Bloo!</sub></h6>

