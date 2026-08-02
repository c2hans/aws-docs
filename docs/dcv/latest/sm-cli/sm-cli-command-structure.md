---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/sm-cli-command-structure.html
---

# Using the command structure
<a name="sm-cli-command-structure"></a>

This topic covers how the Amazon DCV Session Manager CLI command is structured. The CLI uses a multipart structure on the command line that must be specified in this order:

1. `./dcvsm`–The base call to the program.

1. `[options]`– Corresponds to common options that's used by all the commands. You can specify these in any order.

1. `commands`– Specifies which operation to perform.

1. `args`– Corresponds to the arguments required by the command. For a list of arguments, see [Amazon DCV Session Manager CLI reference](sm-cli-reference.md).

## Syntax reference
<a name="sytnax"></a>

```
dcvsm {{[options]}} commands {{args}}
```

Arguments can take various types of input values. These include numbers, strings, boolean. What is supported is dependent upon the command that you specify.
