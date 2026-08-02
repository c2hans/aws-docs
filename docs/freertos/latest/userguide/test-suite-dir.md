---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-dir.html
---

# Create a test suite directory
<a name="test-suite-dir"></a>

IDT logically separates test cases into test groups within each test suite. Each test case must be inside a test group. For this tutorial, create a folder called `MyTestSuite_1.0.0` and create the following directory tree within this folder:

```
MyTestSuite_1.0.0
└── suite
    └── myTestGroup
        └── myTestCase
```
