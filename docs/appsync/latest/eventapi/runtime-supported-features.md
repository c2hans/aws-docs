---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-supported-features.html
---

# Supported runtime features
<a name="runtime-supported-features"></a>

The APPSYNC\_JS runtime supports the features described in the following sections.

**Topics**
+ [Core features](#core-features)
+ [Primitive objects](#primitive-objects)
+ [Built-in objects and functions](#built-in-objects-functions)
+ [Globals](#globals)
+ [Error types](#error-types)

## Core features
<a name="core-features"></a>

The following core features are supported.

**Types**
The following types are supported:
+ numbers
+ strings
+ booleans
+ objects
+ arrays
+ functions

**Operators**
The following operators are supported:
+ standard math operators (`+`, `-`, `/`, `%`, `*`, etc.)
+ nullish coalescing operator (`??`)
+ Optional chaining (`?.`)
+ bitwise operators
+ `void` and `typeof` operators
+ spread operators (`...`)
The following operators are not supported:
+ unary operators (`++`, `--`, and `~`)
+ `in` operator
**Note**
Use the `Object.hasOwn` operator to check if the specified property is in the specified object.

**Statements**
The following statements are supported:
+ `const`
+ `let`
+ `var`
+ `break`
+ `else`
+ `for-in`
+ `for-of`
+ `if`
+ `return`
+ `switch`
+ spread syntax
The following are not supported:
+ `catch`
+ `continue`
+ `do-while`
+ `finally`
+ `for(initialization; condition; afterthought)`
**Note**
The exceptions are `for-in` and `for-of` expressions, which are supported.
+ `throw`
+ `try`
+ `while`
+ labeled statements

**Literals**
The following ES 6 [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) are supported:
+ Multi-line strings
+ Expression interpolation
+ Nesting templates

**Functions**
The following function syntax is supported:
+ Function declarations are supported.
+ ES 6 arrow functions are supported.
+ ES 6 rest parameter syntax is supported.

## Primitive objects
<a name="primitive-objects"></a>

The following primitive objects of ES and their functions are supported.

**Object**
The following objects are supported:
+ `Object.assign()`
+ `Object.entries()`
+ `Object.hasOwn()`
+ `Object.keys()`
+ `Object.values()`
+ `delete`

**String**
The following strings are supported:
+  `String.prototype.length()`
+  `String.prototype.charAt()`
+  `String.prototype.concat()`
+  `String.prototype.endsWith()`
+  `String.prototype.indexOf()`
+  `String.prototype.lastIndexOf()`
+  `String.raw()`
+  `String.prototype.replace()`
**Note**
Regular expressions are not supported.
However, Java-styled regular expression constructs are supported in the provided parameter. For more information see [Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).
+ `String.prototype.replaceAll()`
**Note**
Regular expressions are not supported.
However, Java-styled regular expression constructs are supported in the provided parameter. For more information see [Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).
+  `String.prototype.slice()`
+  `String.prototype.split()`
+  `String.prototype.startsWith()`
+  `String.prototype.toLowerCase()`
+  `String.prototype.toUpperCase()`
+  `String.prototype.trim()`
+  `String.prototype.trimEnd()`
+  `String.prototype.trimStart()`

**Number**
The following numbers are supported:
+  `Number.isFinite`
+  `Number.isNaN`

## Built-in objects and functions
<a name="built-in-objects-functions"></a>

The following functions and objects are supported.

**Math**
+  `Math.random()`
+  `Math.min()`
+  `Math.max()`
+  `Math.round()`
+  `Math.floor()`
+  `Math.ceil()`

**Array**
+ `Array.prototype.length`
+ `Array.prototype.concat()`
+ `Array.prototype.fill()`
+ `Array.prototype.flat()`
+ `Array.prototype.indexOf()`
+ `Array.prototype.join()`
+ `Array.prototype.lastIndexOf()`
+ `Array.prototype.pop()`
+ `Array.prototype.push()`
+ `Array.prototype.reverse()`
+ `Array.prototype.shift()`
+ `Array.prototype.slice()`
+ `Array.prototype.sort()`
**Note**
`Array.prototype.sort()` doesn't support arguments.
+ `Array.prototype.splice()`
+ `Array.prototype.unshift()`
+ `Array.prototype.forEach()`
+ `Array.prototype.map()`
+ `Array.prototype.flatMap()`
+ `Array.prototype.filter()`
+ `Array.prototype.reduce()`
+ `Array.prototype.reduceRight()`
+ `Array.prototype.find()`
+ `Array.prototype.some()`
+ `Array.prototype.every()`
+ `Array.prototype.findIndex()`
+ `Array.prototype.findLast()`
+ `Array.prototype.findLastIndex()`
+ `delete`

**Console**
The console object is available for debugging. During live query execution, console log/error statements are sent to Amazon CloudWatch Logs (if logging is enabled). During code evaluation with `evaluateCode`, log statements are returned in the command response.
+ `console.error()`
+ `console.log()`

**Function**
+ The `apply`, `bind`, and `call` methods not are supported.
+ Function constructors are not supported.
+ Passing a function as an argument is not supported.
+ Recursive function calls are not supported.

**JSON**
The following JSON methods are supported:
+ `JSON.parse()`
**Note**
Returns a blank string if the parsed string is not valid JSON.
+ `JSON.stringify()`

**Promises**
Async processes are not supported, and promises are not supported.
Network and file system access is not supported within the `APPSYNC_JS` runtime in AWS AppSync. AWS AppSync handles all I/O operations based on the requests made by the AWS AppSync handler or AWS AppSync function.

## Globals
<a name="globals"></a>

The following global constants are supported:
+  `NaN`
+  `Infinity`
+  `undefined`
+ `util`
+ `extensions`
+ `runtimeb`

## Error types
<a name="error-types"></a>

Throwing errors with `throw` is not supported. You can return an error by using `util.error()` function. You can include an error in your handler response by using the `util.appendError` function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
