---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-find-apps-using-v1.html
---

# Find applications using AWS SDK for Java 1.x clients
<a name="migration-find-apps-using-v1"></a>

Before migrating to the AWS SDK for Java 2.x, you need to identify which applications in your environment use SDK for Java 1.x clients. You can use CloudTrail logs to trace SDK usage, search application logs for deprecation warnings, inspect your source code and build configurations, or examine your deployable Java artifacts. Use whichever methods are available in your environment.

## Use CloudWatch Logs Insights to find applications with 1.x clients
<a name="migration-find-v1-apps-with-cw-logs-insights"></a>

Amazon CloudWatch Logs Insights lets you query CloudTrail events delivered to a CloudWatch Logs log group. Use this method to identify SDK versions from the *userAgent* field in CloudTrail records. You need a CloudTrail trail with **CloudWatch Logs** enabled. If you don't have one, see [Creating a trail with the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) and [Sending events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html).

In the CloudWatch console, navigate to **Logs Insights** under **Logs**. Select your CloudTrail log group and set the time range to cover the period you want to analyze. For details on using Logs Insights, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

The following sample queries find all requests from user applications and third-party tools made with SDK for Java 1.x. Logs Insights supports both Logs Insights QL and SQL. The QL query uses the log group selected in the console. The SQL query requires you to specify the log group name in the `FROM` clause.

Logs Insights QL query:

```
fields userIdentity.type, userIdentity.arn, eventSource, awsRegion,
       eventName, eventType, eventTime, userAgent, sourceIPAddress
| filter userAgent like /aws-sdk-java\/1\./
| filter userAgent not like /aws-internal\//
| sort eventTime desc
```

SQL query:

```
SELECT `userIdentity.type`,
       `userIdentity.arn`,
       eventSource,
       awsRegion,
       eventName,
       eventType,
       eventTime,
       userAgent,
       sourceIPAddress
  FROM `{{sample-cloudtrail-log-group}}`
 WHERE userAgent LIKE '%aws-sdk-java/1.%'
   AND userAgent NOT LIKE '%aws-internal/%'
 ORDER BY eventTime DESC
```

Replace {{sample-cloudtrail-log-group}} with the name of your CloudTrail log group.

To export the results, choose **Export results**. The following example shows a single event in JSON format:

```
{
  "userIdentity.type": "AssumedRole",
  "userIdentity.arn": "arn:aws:sts::123456789012:assumed-role/Admin/Alice",
  "eventSource": "dynamodb.amazonaws.com",
  "awsRegion": "us-east-1",
  "eventName": "ListTables",
  "eventType": "AwsApiCall",
  "eventTime": "2025-07-01T22:02:23Z",
  "userAgent": "aws-sdk-java/1.12.746 Linux/5.10.240 OpenJDK/11.0.25+9-LTS ...",
  "sourceIPAddress": "12.345.6.78"
}
```

In this example, a DynamoDB `ListTables` request was made at `2025-07-01T22:02:23 (UTC)` from IP address `12.345.6.78` with the credentials of the assumed role `Admin/Alice`. The *userAgent* field shows that the request was made using SDK for Java version `1.12.746` on a Linux system with JDK 11.

For a description of the fields in the AWS CloudTrail event record, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html).

If CloudTrail is not enabled in your account, contact your organization's AWS account administrator to enable it, or use one of the alternative methods described in the following sections.

CloudWatch Logs Insights charges per query based on the amount of data scanned. If you created a trail specifically for this investigation, consider stopping or deleting it to avoid ongoing charges. For current pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Search application warning-level logs for SDK deprecation
<a name="migration-find-v1-apps-log-warning"></a>

Starting with version 1.12.767 (released on July 30, 2024), the AWS SDK for Java 1.x emits a deprecation warning at application startup. You can search your application logs for this warning to identify which applications and hosts are using SDK for Java 1.x.

The exact wording of the warning depends on the SDK version:
+ Versions 1.12.767 through 1.12.796:

  `WARNING: The AWS SDK for Java 1.x entered maintenance mode starting July 31, 2024 and will reach end of support on December 31, 2025...`
+ Versions 1.12.797 and higher:

  `WARNING: The AWS SDK for Java 1.x reached end of support on December 31, 2025...`

The trailing `...` indicates that the warning message continues with additional text. You can search for the common prefix `The AWS SDK for Java 1.x` to find either version of the warning.

The following example demonstrates searching for this warning using `grep`:

```
grep -r "The AWS SDK for Java 1.x" /path/to/your/application/logs/
```

If the warning is found, the `grep` command prints the matching log lines. If no warning is found, either your application is not using SDK for Java 1.x, or it uses a version earlier than 1.12.767. In that case, use one of the other methods described in this document.

## Search source code and dependencies
<a name="migration-find-v1-apps-source-code"></a>

You can search your codebase and build configuration files for references to the AWS SDK for Java 1.x. The key identifier is the `com.amazonaws` group ID, which is used by all SDK for Java 1.x artifacts.

The following examples demonstrate using `grep` to search for `com.amazonaws` references across common Java project files.

**Example: Search Java source files for SDK for Java 1.x imports (run from project root directory)**

```
grep -r "import com.amazonaws" --include="*.java" .
```

Example output:

```
src/main/java/com/example/App.java:import com.amazonaws.services.s3.AmazonS3;
```

**Note**
The `com.amazonaws` package is also used by libraries that are not part of the SDK for Java 1.x, such as `aws-lambda-java-core`. To confirm an import is from SDK for Java 1.x, check that the corresponding artifact ID in your `pom.xml`, `build.gradle`, or dependency management configuration starts with `aws-java-sdk-`.

**Example: Search Maven `pom.xml` files for SDK for Java 1.x dependencies (run from project root directory)**

```
grep -r "com.amazonaws" --include="pom.xml" .
```

Example output:

```
pom.xml:    <groupId>com.amazonaws</groupId>
```

**Example: Search Gradle build files for SDK for Java 1.x dependencies (run from project root directory)**

```
grep -r "com.amazonaws:aws-java-sdk" --include="*.gradle" .
```

Example output:

```
build.gradle:    implementation 'com.amazonaws:aws-java-sdk-s3:1.12.xxx'
```

The preceding `grep` commands identify SDK for Java 1.x references declared directly in your source and build files. However, your application might also depend on SDK for Java 1.x transitively — through a third-party library that itself depends on the SDK. Use your build tool's dependency tree to find both direct and transitive SDK for Java 1.x dependencies. Choose the example that matches your build system.

**Example: Use Maven to find all transitive SDK for Java 1.x dependencies (run from project root directory)**

```
mvn dependency:tree -Dincludes=com.amazonaws
```

Example output:

```
[INFO] com.example:my-application:jar:1.0-SNAPSHOT
[INFO] +- com.amazonaws:aws-java-sdk-s3:jar:1.12.746:compile
[INFO] |  \- com.amazonaws:aws-java-sdk-core:jar:1.12.746:compile
[INFO] \- some.thirdparty:library:jar:2.3.1:compile
[INFO]    \- com.amazonaws:aws-java-sdk-dynamodb:jar:1.12.600:compile
```

The `-Dincludes=com.amazonaws` flag filters the tree to show only SDK for Java 1.x artifacts. In this example, `aws-java-sdk-s3` is a direct dependency, but `aws-java-sdk-dynamodb` is a transitive dependency brought in by `some.thirdparty:library`.

**Example: Use Gradle to find all transitive SDK for Java 1.x dependencies (run from project root directory)**

```
gradle dependencies --configuration runtimeClasspath | grep "com.amazonaws"
```

Example output:

```
+--- com.amazonaws:aws-java-sdk-s3:1.12.746
|    \--- com.amazonaws:aws-java-sdk-core:1.12.746
\--- com.amazonaws:aws-java-sdk-dynamodb:1.12.600
```

Gradle does not have a built-in dependency filter equivalent to Maven's `-Dincludes`, so piping through `grep` is the simplest approach.

## Inspect deployable Java artifacts
<a name="migration-find-v1-apps-inspect-artifacts"></a>

You can inspect your deployable Java artifacts (JARs, WARs, or EARs) to confirm whether the AWS SDK for Java 1.x is packaged with your application. Java archive files are ZIP-format files. To determine if SDK for Java 1.x is present, look for the file `com/amazonaws/sdk/versionInfo.properties` inside the archive. This file is included in the `aws-java-sdk-core` module and contains the SDK version number.

### Quick check with the `jar` command
<a name="migration-find-v1-apps-jar-command"></a>

For uber-jars where all dependency classes are merged at the top level, list the archive contents and search for the version file:

In the following examples, replace `myapp.jar` with the path to your application's JAR file.

```
jar -tf myapp.jar | grep 'versionInfo.properties'
```

If the SDK is present, the output is:

```
com/amazonaws/sdk/versionInfo.properties
```

If the `jar` command is not available in your environment (for example, JRE-only or minimal container images), you can use `unzip -l` instead:

```
unzip -l myapp.jar | grep 'versionInfo.properties'
```

To print the version:

```
unzip -p myapp.jar com/amazonaws/sdk/versionInfo.properties
```

Example output:

```
platform=java
version=1.12.xxx
```

**Note**
The preceding commands only search top-level entries in uber-jars. They will not find SDK classes in thin JARs (where dependencies are external) or inside nested JARs (such as those in WARs, EARs, or Lambda packages under `lib/` or `WEB-INF/lib/`). For thin JARs, check your build configuration (`pom.xml`, `build.gradle`) or dependency tree instead. For nested JARs, search the bundled JARs using a tool that can read ZIP archives recursively without extracting to disk.

## Use CloudTrail Lake to find applications with 1.x clients
<a name="migration-find-v1-apps-with-cloudtrail"></a>

**Important**
AWS CloudTrail Lake is no longer open to new customers starting May 31, 2026. Existing customers can continue to use the service. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html). For an alternative approach, see [Use CloudWatch Logs Insights to find applications with 1.x clients](#migration-find-v1-apps-with-cw-logs-insights).

AWS CloudTrail Lake lets you query events recorded by CloudTrail. Follow these steps to create a data lake that identifies SDK versions used by your applications:

1. Create a CloudTrail data lake. Refer to the [User guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html) to create an event data store.

1. After you create the data store, examine the record contents. The record body contains fields that determine the requested action, timing, and location. For details, refer to the [User guide for CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html).

1. Run queries against your data. Follow the [User Guide to query and save query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-run-query.html).

The *userAgent* field in each record contains the SDK version that made the request. Use this field to identify applications using SDK for Java 1.x.

The following sample query finds all requests from user applications and third-party tools made with SDK for Java 1.x starting from June 17, 2025, for an EventDatastoreID `sample-Data-Store-Id`:

```
select userIdentity, eventSource, awsRegion,
    eventName, eventType, eventTime, userAgent,
    requestParameters, sourceIPAddress
 from sample-Data-Store-Id
where eventTime > '2025-06-17 00:00:00'
and userAgent like '%aws-sdk-java/1.%'
and userAgent not like '%aws-internal/%'
order by eventTime desc
```

An example of event content in the query result looks like this:

```
{
    "userIdentity": "{
         "type": "IAMUser",
         "principalId": "AIDAJ45Q7YFFAREXAMPLE",
         "arn": "arn:aws:iam::123456789012:user/Alice",
         "accountId": "123456789012",
         "accessKeyId": "",
         "userName": "Alice"
    }",
    "eventSource": "dynamodb.amazonaws.com",
    "awsRegion": "us-west-2",
    "eventName": "ListTables",
    "eventType": "AwsApiCall",
    "eventTime": "2025-07-01 02:23:52.000",
    "userAgent": "aws-sdk-java/1.12.746 Linux/5.10.240 OpenJDK/11.0.25+9-LTS ...",
    "requestParameters": "",
    "sourceIPAddress": "12.345.6.78"
}
```

You can use this information to help determine when and where the request was made.

In the example, a DynamoDB `ListTables` request was made at `2025-07-01 02:23:52 (UTC)` from the IP Address `12.345.6.78` with the credentials of the IAM user named Alice. The *userAgent* field's value shows that the request was made using the AWS SDK for Java version `1.12.746` from a Linux system with JDK 11.

For a description of the fields in the AWS CloudTrail event record, see [CloudTrail record contents for management, data, and network activity events ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html).

If CloudTrail is not enabled in your account, contact your organization's AWS account administrator to enable it, or use one of the alternative methods described in the preceding sections.

CloudTrail Lake charges for data ingested and data scanned per query. To minimize costs, filter queries to specific time ranges and regions. For current pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).
