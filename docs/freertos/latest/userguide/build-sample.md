---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/build-sample.html
---

# Build the sample test suite
<a name="build-sample"></a>

The `{{<device-tester-extract-location>}}/samples/python` folder contains sample configuration files, source code, and the IDT Client SDK that you can combine into a test suite using the provided build scripts. The following directory tree shows the location of these sample files:

```
{{<device-tester-extract-location>}}
├── ...
├── tests
├── samples
│   ├── ...
│   └── python
│       ├── configuration
│       ├── src
│       └── build-scripts
│           ├── build.sh
│           └── build.ps1
└── sdks
    ├── ...
    └── python
        └── idt_client
```

To build the test suite, run the following commands on your host computer:

------
#### [ Windows ]

```
cd {{<device-tester-extract-location>}}/samples/python/build-scripts
./build.ps1
```

------
#### [ Linux, macOS, or UNIX ]

```
cd {{<device-tester-extract-location>}}/samples/python/build-scripts
./build.sh
```

------

This creates the sample test suite in the `IDTSampleSuitePython_1.0.0` folder within the `{{<device-tester-extract-location>}}/tests` folder. Review the files in the `IDTSampleSuitePython_1.0.0` folder to understand how the sample test suite is structured and to see various examples of test case executables and test configuration files.

**Note**
The sample test suite includes python source code. Do not include sensitive information in your test suite code.

Next step: Use IDT to [run the sample test suite](run-sample.md) that you created.
