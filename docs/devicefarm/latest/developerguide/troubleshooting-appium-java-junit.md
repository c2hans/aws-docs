---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/troubleshooting-appium-java-junit.html
---

# Troubleshooting Appium Java JUnit tests in AWS Device Farm

The following topic lists error messages that occur during the upload of Appium Java JUnit tests and recommends workarounds to resolve each error.

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. After you successfully extract the files, you should find at least one class in the working directory tree by running the command:

   ```
   $ tree .
   ```

   You should see output like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `-{{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JUNIT\_VERSION\_VALUE\_UNKNOWN
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We could not find a JUnit version value. Please unzip your test package and open the dependency-jars directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working-directory tree structure by running the following command:

   ```
   tree .
   ```

   The output should look like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
       |— {{junit-4.10.jar}}
       |— com.some-dependency.bar-4.1.jar
       |— com.another-dependency.thing-1.0.jar
       |— joda-time-2.7.jar
       `— log4j-1.2.14.jar
   ```

   If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the jar file {{junit-4.10.jar}} in our example. The name should consist of the keyword {{junit}} and its version number, which in this example is 4.10.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_INVALID\_JUNIT\_VERSION
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**
We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit version and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find a JUnit dependency file like {{junit-4.10.jar}} in our example and its version number, which in our example is 4.10:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```
**Note**
Your tests may not execute correctly if the JUnit version specified in your test package is lower than the minimum version 4.10 we support.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Test insights
<a name="troubleshooting-appium-java-junit-insights"></a>

When test insights are enabled, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for Appium Java JUnit mobile app and web app tests.

### The job did not run to completion
<a name="ti-appium-java-junit-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

### The results contained no test cases
<a name="ti-appium-java-junit-no-test-cases"></a>

`Test insights could not be generated. The JUnit XML was parsed successfully but contained no test cases. Verify that your test suite includes at least one test case and that the JUnit XML is stored correctly in the output artifacts directory.`

The report parsed successfully but declared zero test cases. This happens most often when the selector you passed to the JUnit Platform matched no tests, for example a package or tag that none of your tests carries.

To resolve this issue, verify that your selector matches at least one test and that the reports are under `$DEVICEFARM_LOG_DIR`.

### The test output exceeds the maximum supported size
<a name="ti-appium-java-junit-output-too-large"></a>

`Unable to generate test insights: "JUnit XML" exceeds the maximum supported size of 1GB.`

The collected JUnit XML reports are larger than 1 GB in total.

To resolve this issue, reduce the report size to less than 1 GB. To reduce the size, write less output to `system-out` and `system-err`. The JUnit XML format embeds that output in the report.

### No JUnit XML report was found
<a name="ti-appium-java-junit-report-not-found"></a>

`Unable to generate test insights. The JUnit XML test results file was not found in the output artifacts. Ensure your test framework is configured to produce JUnit XML reports and that the results are written to the artifacts directory.`

`$DEVICEFARM_LOG_DIR` contained no JUnit XML report. JUnit doesn't use a standard report file name, so Device Farm looks for every JUnit XML report under `$DEVICEFARM_LOG_DIR`. A run that prints its results to the console only, without writing a report file, or that writes the report somewhere else, produces nothing to summarize.

To resolve this issue, configure your run to write a report under `$DEVICEFARM_LOG_DIR`. Pass `--reports-dir` on a Console Launcher command, or copy the build tool's own report directory into `$DEVICEFARM_LOG_DIR` in the `post_test` phase of your test spec file. For the options, see [Configure Appium test reports using a custom test environment](test-types-appium-integrate.md#test-types-appium-generate-reports).

### The JUnit XML report could not be processed
<a name="ti-appium-java-junit-report-error"></a>

`Test insights could not be generated due to an error while processing the JUnit XML report. Ensure the file is well-formed XML in the standard JUnit report format.`

The report was malformed or could not be parsed. If a run stops partway through, the report can be truncated.

To resolve this issue, verify that the file is well-formed XML in the standard JUnit report format. If your run writes several reports and only one is malformed, Device Farm reports the tests from the others, so this message means that no report could be read.
