---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-python.html
---

# Troubleshooting Appium Python tests in AWS Device Farm

The following topic lists error messages that occur during the upload of Appium Python tests and recommends workarounds to resolve each error.

## APPIUM\_PYTHON\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Python package should produce output like the following:

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEEL\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PLATFORM
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PLATFORM"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We found at least one wheel file specified a platform that we do not support. Please unzip your test package and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux\_x86\_64.whl, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory. The file's name may be different, but it should end with {{-any.whl}} or {{-linux\_x86\_64.whl}}, which specifies the platform. Any other platforms like `windows` are not supported.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_TEST\_DIR\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find the tests directory inside your test package. Please unzip your test package, verify that the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- {{tests}} (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_TEST\_FILE\_NAME
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a valid test file in the tests directory tree. Please unzip your test package and then open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory. The file's name may be different, but it should start with {{test\_}} or end with {{\_test.py}}.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- {{test_unittest.py}}
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_REQUIREMENTS\_TXT\_FILE\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find the requirements.txt file inside your test package. Please unzip your test package, verify that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PYTEST\_VERSION
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `--test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

1. To get the pytest version, you can run the following command:

   ```
   $ grep "pytest" requirements.txt
   ```

   You should find output like the following:

   ```
   pytest==2.9.0
   ```

   It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the pytest version should be larger than or equal to 2.8.0.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_INSTALL\_DEPENDENCY\_WHEELS\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We failed to install the dependency wheels. Please unzip your test package and then open the requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To test installing wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

   A valid Appium Python package should produce output like the following:

   ```
   Ignoring indexes: https://pypi.python.org/simple
   Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
   Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
   Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
   Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
   Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
   Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
     Found existing installation: wheel 0.29.0
       Uninstalling wheel-0.29.0:
         Successfully uninstalled wheel-0.29.0
   Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_PYTEST\_COLLECT\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We failed to collect tests in the tests directory. Please unzip your test package, very that the test package is valid by running the command `py.test --collect-only <path to your tests directory>`, and try again after the command does not print any error.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To install wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

1. To collect tests, you can run the following command:

   ```
   $ py.test --collect-only tests
   ```

   A valid Appium Python package should produce output like the following:

   ```
   ==================== test session starts ====================
   platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
   rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
   collected 1 items
   <Module 'test_unittest.py'>
     <UnitTestCase 'DeviceFarmAppiumWebTests'>
       <TestCaseFunction 'test_devicefarm'>

   ==================== no tests ran in 0.11 seconds ====================
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEELS\_INSUFFICIENT
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEELS_INSUFFICIENT"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find enough wheel dependencies in the wheelhouse directory. Please unzip your test package, and then open the wheelhouse directory. Verify that you have all the wheel dependencies specified in the requirements.txt file.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. Check the length of the {{requirements.txt}} file as well as the number of {{.whl}} dependent files in the wheelhouse directory:

   ```
   $ cat requirements.txt | egrep "." |wc -l
   ﻿    12
   $ ls wheelhouse/ | egrep ".+\.whl" | wc -l
       11
   ```

   If the number of {{.whl}} dependent files is less than the number of non-empty rows in your {{requirements.txt}} file, then you need to ensure the following:
   + There is a {{.whl}} dependent file corresponding to each row in the {{requirements.txt}} file.
   + There are no other lines in the {{requirements.txt}} file that contain information other than the dependency package names.
   + No dependency names are duplicated in multiple lines in the {{requirements.txt}} file such that two lines in the file may correspond to one {{.whl}} dependent file.

   AWS Device Farm doesn't support lines in the {{requirements.txt}} file that don't directly correspond to dependency packages, such as lines that specify global options for the `pip install` command. See [Requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#global-options) for a list of global options.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Test insights
<a name="troubleshooting-appium-python-insights"></a>

When test insights are enabled, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for Appium Python mobile app and web app tests.

### The job did not run to completion
<a name="ti-appium-python-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

### No JUnit XML test results file was found
<a name="ti-appium-python-no-report"></a>

`Unable to generate test insights. No JUnit XML test results file was found in the output artifacts. Run pytest with --junit-xml and write the report under $DEVICEFARM_LOG_DIR, for example --junit-xml $DEVICEFARM_LOG_DIR/junitreport.xml. Any filename works.`

Device Farm searched your test output artifacts and found no pytest report.

To resolve this issue, check the following:
+ Your test spec runs pytest with the `--junit-xml` option.
+ The report path is under `$DEVICEFARM_LOG_DIR`, and the file name ends in `.xml`.
+ The test session ran to the end. pytest writes the report when the session finishes, so a session that stops early, for example at the job timeout, writes no report. A `conftest.py` that fails to import stops the session before any test runs.

### The test report could not be processed
<a name="ti-appium-python-report-error"></a>

`Test insights could not be generated due to an error while processing the pytest JUnit XML report. Ensure the file is well-formed XML in the standard JUnit report format.`

Device Farm found one or more reports but could not read any of them. If some reports can be read, Device Farm uses those and skips the rest, so this message means that none could be read. The usual cause is a report that was truncated or rewritten after pytest wrote it.

To resolve this issue, verify that your test spec does not move, rewrite, or compress the report after pytest writes it.

### The results contained no test cases
<a name="ti-appium-python-no-test-cases"></a>

`Test insights could not be generated. The pytest JUnit XML was parsed successfully but contained no test cases. Verify that your test suite includes at least one test case and that the pytest JUnit XML is stored correctly in the output artifacts directory.`

The report parsed successfully but contained zero test cases.

To resolve this issue, verify that pytest collects at least one test from the paths in your test spec. A `-k` or `-m` expression that matches no test produces a report with no test cases.

### The test report exceeds the maximum supported size
<a name="ti-appium-python-report-too-large"></a>

`Unable to generate test insights: "pytest JUnit XML" exceeds the maximum supported size of 250MB.`

The only report that Device Farm found in your test output artifacts is larger than 250 MB, so it could not be read. If the archive holds another readable report, Device Farm uses that report and ignores the oversized one, and this message does not appear.

To resolve this issue, reduce the size of the report. Captured output and long tracebacks are the usual causes. Remove the `junit_logging` setting if you set it, and consider the `--tb=short` option.

### The test output archive is not a valid zip file
<a name="ti-appium-python-invalid-archive"></a>

`Unable to generate test insights: the test output archive could not be processed because it is not a valid zip file.`

The archive (zip file) that contains your test output artifacts could not be opened.

To resolve this issue, retry the run. If the error persists, contact AWS Support.

### A service error occurred
<a name="ti-appium-python-service-error"></a>

`Test insights could not be generated due to a service error.`

Device Farm could not collect the artifacts it needs to summarize the job. This message also appears when the archive (zip file) that contains your test output artifacts is larger than 1 GB.

To resolve this issue, reduce what your tests write to `$DEVICEFARM_LOG_DIR`, and retry the run. If the error persists, contact AWS Support.
