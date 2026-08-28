---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-json.html
---

# Create configuration files
<a name="test-suite-json"></a>

Your test suite must contain the following required [configuration files](idt-json-config.md):

**Required files**

**`suite.json`**
Contains information about the test suite. See [Configure suite.json](idt-json-config.md#suite-json).

**`group.json`**
Contains information about a test group. You must create a `group.json` file for each test group in your test suite. See [Configure group.json](idt-json-config.md#group-json).

**`test.json`**
Contains information about a test case. You must create a `test.json` file for each test case in your test suite. See [Configure test.json](idt-json-config.md#test-json).

1. In the `MyTestSuite_1.0.0/suite` folder, create a `suite.json` file with the following structure:

   ```
   {
       "id": "MyTestSuite_1.0.0",
       "title": "My Test Suite",
       "details": "This is my test suite.",
       "userDataRequired": false
   }
   ```

1. In the `MyTestSuite_1.0.0/myTestGroup` folder, create a `group.json` file with the following structure:

   ```
   {
       "id": "MyTestGroup",
       "title": "My Test Group",
       "details": "This is my test group.",
       "optional": false
   }
   ```

1. In the `MyTestSuite_1.0.0/myTestGroup/myTestCase` folder, create a `test.json` file with the following structure:

   ```
   {
       "id": "MyTestCase",
       "title": "My Test Case",
       "details": "This is my test case.",
       "execution": {
           "timeout": 300000,
           "linux": {
               "cmd": "python3",
               "args": [
                   "myTestCase.py"
               ]
           },
           "mac": {
               "cmd": "python3",
               "args": [
                   "myTestCase.py"
               ]
           },
           "win": {
               "cmd": "python3",
               "args": [
                   "myTestCase.py"
               ]
           }
       }
   }
   ```

The directory tree for your `MyTestSuite_1.0.0` folder should now look like the following:

```
MyTestSuite_1.0.0
└── suite
    ├── suite.json
    └── myTestGroup
        ├── group.json
        └── myTestCase
            └── test.json
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
