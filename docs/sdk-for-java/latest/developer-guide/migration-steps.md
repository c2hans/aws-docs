---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-steps.html
---

# Migration step-by-step instructions with example
<a name="migration-steps"></a>

This section provides a step-by-step guide to migrate your application that currently uses the SDK for Java v1.x to the SDK for Java 2.x. The first part presents an overview of the steps followed by a detailed example of a migration.

The steps that are covered here describe a migration of a normal use case, where the application calls AWS services using model-driven service clients. If you need to migrate code that uses higher level APIs such as [S3 Transfer Manager](migration-s3-transfer-manager.md) or [CloudFront presigning](migration-cloudfront-presigning.md), refer to the section under [What's different between the AWS SDK for Java 1.x and 2.x](migration-whats-different.md) table of contents.

The approach described here is a suggestion. You may use other techniques and leverage your IDE's code editing features to reach the same result.

## Overview of steps
<a name="migration-steps-overview"></a>

### 1. Begin by adding the SDK for Java 2.x BOM
<a name="migration-steps-overview-step1"></a>

By adding the Maven BOM (Bill of Materials) element for the SDK for Java 2.x to your POM file, you ensure that all of the v2 dependency you need are from the same version. Your POM can contain both v1 and v2 dependencies. This allows you to incrementally migrate your code rather than change it all at once.

#### SDK for Java 2.x BOM
<a name="drt_b5n_q1c"></a>

```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>bom</artifactId>
      <version>{{2.27.21}}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

You can find the [latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom) on the Maven Central Repository.

### 2. Search files for v1 class import statements
<a name="migration-steps-overview-step2"></a>

By scanning the files in your application for SERVICE\_IDs used in v1 imports, you'll find the unique SERVICE\_IDs used. A SERVICE\_ID is a short, unique name for an AWS service. For example `cognitoidentity` is the SERVICE\_ID for Amazon Cognito Identity.

### 3. Determine the v2 Maven dependencies from the v1 import statements
<a name="migration-steps-overview-step3"></a>

After you find all unique v1 SERVICE\_IDs, you can determine the corresponding Maven artifact for the v2 dependency by referring to [Package name to Maven artifactId mappings](#migration-serviceid-artifactid-mapping).

### 4. Add v2 dependency elements to the POM file
<a name="migration-steps-overview-step4"></a>

Update the Maven POM file with dependency elements determined in step 3.

### 5. In the Java files, incrementally change over the v1 classes to v2 classes
<a name="migration-steps-overview-step5"></a>

As you replace v1 classes with v2 classes, make the necessary changes to support the v2 API such as using builders instead of constructors and using fluent getters and setters.

### 6. Remove v1 Maven dependencies from the POM and v1 imports from files
<a name="migration-steps-overview-step6"></a>

After you migrate your code to use v2 classes, remove any leftover v1 imports from files and all dependencies from your build file.

### 7. Refactor the code to use v2 API enhancements
<a name="migration-steps-overview-step7"></a>

After the code successfully compiles and passes tests, you can take advantage of v2 enhancements such as using a different HTTP client or paginators to simplify code. This is an optional step.

## Example migration
<a name="migration-steps-example"></a>

In this example, we migrate an application that uses the SDK for Java v1 and accesses several AWS services. We work through the following v1 method in detail in step 5. This is one method in a class that contains eight methods and there are 32 classes in the application.

### v1 method to migrate
<a name="v1-snippet-collapsed"></a>

Only the v1 SDK imports are listed below from the Java file.

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.RegionUtils;
import com.amazonaws.services.ec2.AmazonEC2Client;
import com.amazonaws.services.ec2.model.AmazonEC2Exception;
import com.amazonaws.services.ec2.model.CreateTagsRequest;
import com.amazonaws.services.ec2.model.DescribeInstancesRequest;
import com.amazonaws.services.ec2.model.DescribeInstancesResult;
import com.amazonaws.services.ec2.model.Instance;
import com.amazonaws.services.ec2.model.InstanceStateName;
import com.amazonaws.services.ec2.model.Reservation;
import com.amazonaws.services.ec2.model.Tag;
import com.amazonaws.services.ec2.model.TerminateInstancesRequest;
...
private static List<Instance> getRunningInstances(AmazonEC2Client ec2, List<String> instanceIds) {
    List<Instance> runningInstances = new ArrayList<>();
    try {
        DescribeInstancesRequest request = new DescribeInstancesRequest()
                .withInstanceIds(instanceIds);
        DescribeInstancesResult result;
        do {
            // DescribeInstancesResponse is a paginated response, so use tokens with multiple requests.
            result = ec2.describeInstances(request);
            request.setNextToken(result.getNextToken());   // Prepare request for next page.
            for (final Reservation r : result.getReservations()) {
                for (final Instance instance : r.getInstances()) {
                    LOGGER.info("Examining instanceId: "+ instance.getInstanceId());
                    // if instance is in a running state, add it to runningInstances list.
                    if (RUNNING_STATES.contains(instance.getState().getName())) {
                        runningInstances.add(instance);
                    }
                }
            }
        } while (result.getNextToken() != null);
    } catch (final AmazonEC2Exception exception) {
        // if instance isn't found, assume its terminated and continue.
        if (exception.getErrorCode().equals(NOT_FOUND_ERROR_CODE)) {
            LOGGER.info("Instance probably terminated; moving on.");
        } else {
            throw exception;
        }
    }
    return runningInstances;
}
```

### 1. Add v2 Maven BOM
<a name="migration-steps-example-step1"></a>

Add the Maven BOM for the SDK for Java 2.x to the POM along side any other dependencies in the `dependencyManagement` section. If your POM file has the BOM for v1 of the SDK, leave it for now. It will be removed at a later step.

#### POM Dependency management at outset
<a name="migration-example-boms"></a>

```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.example</groupId>             <!--Existing dependency in POM. -->
      <artifactId>bom</artifactId>
      <version>1.3.4</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    ...
    <dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-java-sdk-bom</artifactId>  <!--Existing v1 BOM dependency. -->
      <version>1.11.1000</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    ...
    <dependency>
      <groupId>software.amazon.awssdk</groupId>  <!--Add v2 BOM dependency. -->
      <artifactId>bom</artifactId>
      <version>{{2.27.21}}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

### 2. Search files for v1 class import statements
<a name="migration-steps-example-step2"></a>

Search the application's code for unique occurrences of `import com.amazonaws.services`. This helps us determine the v1 dependencies used by the project. If your application has a Maven POM file with v1 dependencies listed, you can use this information instead.

For this example we use the [`ripgrep` (rg)](https://github.com/BurntSushi/ripgrep) command to search the code base.

From the root of your code base, execute the following `ripgrep` command. After `ripgrep` finds the import statements, they are piped to the `cut`, `sort`, and `uniq` commands to isolate the SERVICE\_IDs.

```
rg --no-filename 'import\s+com\.amazonaws\.services' | cut -d '.' -f 4 | sort | uniq
```

For this application, the following SERVICE\_IDs are logged to the console.

```
autoscaling
cloudformation
ec2
identitymanagement
```

This indicates that there was at least one occurrence of each of the following package names used in `import` statements. For our purposes, the individual class names don't matter. We just need to find the SERVICE\_IDs that are used.

```
com.amazonaws.services.autoscaling.*
com.amazonaws.services.cloudformation.*
com.amazonaws.services.ec2.*
com.amazonaws.services.identitymanagement.*
```

### 3. Determine the v2 Maven dependencies from the v1 import statements
<a name="migration-steps-example-step3"></a>

The SERVICE\_IDs for v1 that we isolated from Step 2—for example `autoscaling` and `cloudformation`—can be mapped to the same v2 SERVICE\_ID for the most part. Since the v2 Maven artifactId matches the SERVICE\_ID in most cases, you have the information you need to add dependency blocks to your POM file.

The following table shows how we can determine the v2 dependencies.

| v1 SERVICE\_ID maps to ...package name | v2 SERVICE\_ID maps to ...package name | v2 Maven dependency |
| --- | --- | --- |
| **ec2**<br />`com.amazonaws.services.ec2.*` | **ec2**<br />`software.amazon.awssdk.services.ec2.*` |  <pre><dependency><br />  <groupId>software.amazon.awssdk</groupId><br />  <artifactId>ec2</artifactId><br /></dependency></pre>  |
| **autoscaling**<br />`com.amazonaws.services.autoscaling.*` | **autoscaling**<br />`software.amazon.awssdk.services.autoscaling.*` |  <pre><dependency><br />  <groupId>software.amazon.awssdk</groupId><br />  <artifactId>autoscaling</artifactId><br /></dependency></pre>  |
| cloudformation`com.amazonaws.services.cloudformation.*` | cloudformation`software.amazon.awssdk.cloudformation.*` |  <pre><dependency><br />  <groupId>software.amazon.awssdk</groupId><br />  <artifactId>cloudformation</artifactId><br /></dependency></pre>  |
| identitymanagement\*`com.amazonaws.services.identitymanagement.*` | iam\*`software.amazon.awssdk.iam.*` |  <pre><dependency><br />  <groupId>software.amazon.awssdk</groupId><br />  <artifactId>iam</artifactId><br /></dependency></pre>  |

\* The `identitymanagement` to `iam` mapping is an exception where the SERVICE\_ID differs between versions. Refer to the [Package name to Maven artifactId mappings](#migration-serviceid-artifactid-mapping) for exceptions if Maven or Gradle cannot resolve the v2 dependency.

### 4. Add v2 dependency elements to the POM file
<a name="migration-steps-example-step4"></a>

In step 3, we determined the four dependency blocks that need to be added to the POM file. We don't need to add a version because we have specified the BOM in step 1. After the imports are added, our POM file has the following dependency elements.

```
    ...
  <dependencies>
    ...
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>autoscaling</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>iam</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>cloudformation</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>ec2</artifactId>
    </dependency>
    ...
  </dependencies>
    ...
```

### 5. In the Java files, incrementally change over the v1 classes to v2 classes
<a name="migration-steps-example-step5"></a>

In the method that we are migrating, we see
+ An EC2 service client from `com.amazonaws.services.ec2.AmazonEC2Client`.
+ Several EC2 model classes used. For example `DescribeInstancesRequest` and `DescribeInstancesResult`.

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.RegionUtils;
import com.amazonaws.services.ec2.AmazonEC2Client;
import com.amazonaws.services.ec2.model.AmazonEC2Exception;
import com.amazonaws.services.ec2.model.CreateTagsRequest;
import com.amazonaws.services.ec2.model.DescribeInstancesRequest;
import com.amazonaws.services.ec2.model.DescribeInstancesResult;
import com.amazonaws.services.ec2.model.Instance;
import com.amazonaws.services.ec2.model.InstanceStateName;
import com.amazonaws.services.ec2.model.Reservation;
import com.amazonaws.services.ec2.model.Tag;
import com.amazonaws.services.ec2.model.TerminateInstancesRequest;
...
private static List<Instance> getRunningInstances(AmazonEC2Client ec2, List<String> instanceIds)
    List<Instance> runningInstances = new ArrayList<>();
    try {
        DescribeInstancesRequest request = new DescribeInstancesRequest()
                .withInstanceIds(instanceIds);
        DescribeInstancesResult result;
        do {
            // DescribeInstancesResponse is a paginated response, so use tokens with multiple re
            result = ec2.describeInstances(request);
            request.setNextToken(result.getNextToken());   // Prepare request for next page.
            for (final Reservation r : result.getReservations()) {
                for (final Instance instance : r.getInstances()) {
                    LOGGER.info("Examining instanceId: "+ instance.getInstanceId());
                    // if instance is in a running state, add it to runningInstances list.
                    if (RUNNING_STATES.contains(instance.getState().getName())) {
                        runningInstances.add(instance);
                    }
                }
            }
        } while (result.getNextToken() != null);
    } catch (final AmazonEC2Exception exception) {
        // if instance isn't found, assume its terminated and continue.
        if (exception.getErrorCode().equals(NOT_FOUND_ERROR_CODE)) {
            LOGGER.info("Instance probably terminated; moving on.");
        } else {
            throw exception;
        }
    }
    return runningInstances;
}
...
```

Our goal is to replace all v1 imports with v2 imports. We proceed one class at a time.

#### a. Replace import statement or class name
<a name="migration-example-step5-substep1"></a>

We see that the first parameter to the `describeRunningInstances` method is a v1 `AmazonEC2Client` instance. Do one of the following:
+ Replace the import for `com.amazonaws.services.ec2.AmazonEC2Client` with `software.amazon.awssdk.services.ec2.Ec2Client` and change `AmazonEC2Client` to `Ec2Client`.
+ Change the parameter type to `Ec2Client` and let the IDE prompt us for the correct import. Our IDE will prompt us to import the v2 class because the client names differ—`AmazonEC2Client` and `Ec2Client`. This approach does not work if the class name is the same in both versions.

#### b. Replace v1 model classes with v2 equivalents
<a name="migration-example-step5-substep2"></a>

After the change to the v2 `Ec2Client`, if we use an IDE, we see compilation errors in the following statement.

```
                    result = ec2.describeInstances(request);
```

The compilation error results from using an instance of v1's `DescribeInstancesRequest` as a parameter to the v2 `Ec2Client` `describeInstances` method. To fix, make the following replacement or import statements.

| replace | with |
| --- | --- |
|  <pre>import com.amazonaws.services.ec2.model.DescribeInstancesRequest</pre>  |  <pre>import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest</pre>  |

#### c. Change v1 constructors to v2 builders.
<a name="migration-example-step5-substep3"></a>

We still see compilation errors because there are [no constructors on v2 classes](migration-whats-different.md#immutable-classes). To fix, make the following change.

| change | to |
| --- | --- |
|  <pre>final DescribeInstancesRequest request = new DescribeInstancesRequest()<br />        .withInstanceIds(instanceIdsCopy);</pre>  |  <pre>final DescribeInstancesRequest request = DescribeInstancesRequest.builder()<br />        .instanceIds(instanceIdsCopy)<br />        .build();</pre>  |

#### d. Replace v1 `*Result` response objects with v2 `*Response` equivalents
<a name="migration-example-step5-substep4"></a>

A consistent difference between v1 and v2 is that all [response objects in v2 end with `*Response` instead of `*Result`](migration-whats-different.md#model-classname-changes). Replace the v1 `DescribeInstancesResult` import to the v2 import, `DescribeInstancesResponse`.

#### d. Make API changes
<a name="migration-example-step5-substep5"></a>

The following statement needs a few changes.

```
request.setNextToken(result.getNextToken());
```

In v2, [setter methods](migration-whats-different.md#setter-getter-methods) do not use the `set` or with `prefix`. Getter methods prefixed with `get` are also gone in the SDK for Java 2.x

Model classes, such as the `request` instance, are immutable in v2, so we need to create a new `DescribeInstancesRequest` with a builder.

In v2, the statement becomes the following.

```
request = DescribeInstancesRequest.builder()
        .nextToken(result.nextToken())
        .build();
```

#### d. Repeat until method compiles with v2 classes
<a name="migration-example-step5-substep6"></a>

Continue with the rest of the code. Replace v1 imports with v2 imports and fix the compilation errors. Refer to the [v2 API Reference](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/package-summary.html) and [What's different reference](migration-whats-different.md) as needed.

After we migrate this single method, we have the following v2 code.

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.RegionUtils;
import com.amazonaws.services.ec2.AmazonEC2Client;
import com.amazonaws.services.ec2.model.AmazonEC2Exception;
import com.amazonaws.services.ec2.model.CreateTagsRequest;
import com.amazonaws.services.ec2.model.InstanceStateName;
import com.amazonaws.services.ec2.model.Tag;
import com.amazonaws.services.ec2.model.TerminateInstancesRequest;

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;
import software.amazon.awssdk.services.ec2.model.Instance;
import software.amazon.awssdk.services.ec2.model.Reservation;
...
private static List<Instance> getRunningInstances(Ec2Client ec2, List<String> instanceIds) {
    List<Instance> runningInstances = new ArrayList<>();
        try {
            DescribeInstancesRequest request = DescribeInstancesRequest.builder()
                    .instanceIds(instanceIds)
                    .build();
            DescribeInstancesResponse result;
            do {
                // DescribeInstancesResponse is a paginated response, so use tokens with multiple re
                result = ec2.describeInstances(request);
                request = DescribeInstancesRequest.builder()   // Prepare request for next page.
                        .nextToken(result.nextToken())
                        .build();
                for (final Reservation r : result.reservations()) {
                    for (final Instance instance : r.instances()) {
                        // if instance is in a running state, add it to runningInstances list.
                        if (RUNNING_STATES.contains(instance.state().nameAsString())) {
                            runningInstances.add(instance);
                        }
                    }
                }
            } while (result.nextToken() != null);
        } catch (final Ec2Exception exception) {
            // if instance isn't found, assume its terminated and continue.
            if (exception.awsErrorDetails().errorCode().equals(NOT_FOUND_ERROR_CODE)) {
                    LOGGER.info("Instance probably terminated; moving on.");
            } else {
                throw exception;
            }
        }
        return runningInstances;
    }
...
```

Because we are migrating a single method in a Java file with eight methods, we have a mix of v1 and v2 imports as we work through the file. We added the last six import statements as we performed the steps.

After we migrate all the code, there will be no more v1 import statements.

### 6. Remove v1 Maven dependencies from the POM and v1 imports from files
<a name="migration-steps-example-step6"></a>

After we migrate all v1 code in the file, we have the following v2 SDK import statements.

```
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.regions.ServiceMetadata;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.CreateTagsRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;
import software.amazon.awssdk.services.ec2.model.Instance;
import software.amazon.awssdk.services.ec2.model.InstanceStateName;
import software.amazon.awssdk.services.ec2.model.Reservation;
import software.amazon.awssdk.services.ec2.model.Tag;
import software.amazon.awssdk.services.ec2.model.TerminateInstancesRequest;
```

After we migrate *all* files in our application, we no longer need the v1 dependencies in our POM file. Remove the v1 BOM from the `dependencyManagement` section, if using, and all v1 dependency blocks.

### 7. Refactor the code to use v2 API enhancements
<a name="migration-steps-example-step7"></a>

For the snippet we have been migrating, we can optionally use a v2 paginator and let the SDK manage the token-based requests for more data.

We can replace the entire `do` clause with the following.

```
                DescribeInstancesIterable responses = ec2.describeInstancesPaginator(request);

                responses.reservations().stream()
                        .forEach(reservation -> reservation.instances()
                                .forEach(instance -> {
                                    if (RUNNING_STATES.contains(instance.state().nameAsString())) {
                                        runningInstances.put(instance.instanceId(), instance);
                                    }
                                }));
```

## Package name to Maven artifactId mappings
<a name="migration-serviceid-artifactid-mapping"></a>

When you migrate your Maven or Gradle project from v1 of the SDK for Java to v2, you need to figure out which dependencies to add to your build file. The approach described in the [Migration step-by-step instructions with example](#migration-steps) (step 3) uses the package names in import statements as a starting point to determine the dependencies (as artifactIds) to add to your build file.

You can use the information in this topic to map the v1 package names to v2 artifactIds.

### Common naming convention used in package names and Maven artifactIds
<a name="migration-naming-convention"></a>

The following table shows the common naming convention that the SDKs use for a given SERVICE\_ID. A SERVICE\_ID is a unique identifier for an AWS service. For example, the SERVICE\_ID for the Amazon S3 service is `s3` and `cognitoidentity` is the SERVICE\_ID for Amazon Cognito Identity.

<table>
<thead>
  <tr><th>v1 package name (import statement)</th><th>v1 artifactId</th><th>v2 artifactId</th><th>v2 package name (import statement)</th></tr>
</thead>
<tbody>
  <tr><td>com.amazonaws.services.SERVICE\_ID</td><td>aws-java-sdk-SERVICE\_ID</td><td>SERVICE\_ID</td><td>software.amazon.awssdk.services.SERVICE\_ID</td></tr>
  <tr><td colspan="4"> </td></tr>
  <tr><td colspan="4">Example for Amazon Cognito Identity (SERVICE\_ID: cognitoidentity)</td></tr>
  <tr><td>com.amazonaws.services.cognitoidentity</td><td>aws-java-sdk-cognitoidentity</td><td>cognitoidentity</td><td>software.amazon.awssdk.services.cognitoidentity</td></tr>
</tbody>
</table>

### SERVICE\_ID differences
<a name="migration-serviceid-diffs"></a>

#### Within v1
<a name="migration-serviceid-diffs-withinv1"></a>

In some cases the SERVICE\_ID differs between the package name and in the artifactId for the same service. For example, the CloudWatch Metrics row of the following table shows that `metrics` is the SERVICE\_ID in the package name but `cloudwatchmetrics` is the artifactId's SERVICE\_ID.

#### Within v2
<a name="migration-serviceid-diffs-withinv2"></a>

There are no differences in the SERVICE\_ID used in package names and artifactIds.

#### Between v1 and v2
<a name="migration-serviceid-diffs-btwv1v2"></a>

For the majority of services, the SERVICE\_ID in v2 is the same as v1's SERVICE\_ID in both package names and artifactIds. An example of this is the `cognitoedentity` SERVICE\_ID as shown in the previous table. However, some SERVICE\_IDs differ between the SDKs as shown in the following table.

A **boldface SERVICE\_ID** in either of the v1 columns indicates that it's different from the SERVICE\_ID used in v2.

<table>
<thead>
  <tr><th>Service name</th><th>v1 package name</th><th>v1 artifactId</th><th>v2 artifactId</th><th>v2 package name</th></tr>
</thead>
<tbody>
  <tr><td></td><td>All package names begin with `com.amazonaws.services` as shown in the first row.</td><td>All artifactIds are enclosed in tags as shown in the first row.</td><td>All artifactIds are enclosed in tags as shown in the first row.</td><td>All package names begin with `software.amazon.awssdk` as shown in the first row.</td></tr>
  <tr><td colspan="5"></td></tr>
  <tr><td>API Gateway</td><td>com.amazonaws.services.apigateway</td><td><artifactId>aws-java-sdk-api-gateway</artifactId></td><td><artifactId>apigateway</artifactId></td><td>software.amazon.awssdk.services.apigateway</td></tr>
  <tr><td>App Registry</td><td>appregistry</td><td>appregistry</td><td>servicecatalogappregistry</td><td>servicecatalogappregistry</td></tr>
  <tr><td>Application Discovery</td><td>applicationdiscovery</td><td>discovery</td><td>applicationdiscovery</td><td>applicationdiscovery</td></tr>
  <tr><td>Augmented AI Runtime</td><td>augmentedairuntime</td><td>augmentedairuntime</td><td>sagemakera2iruntime</td><td>sagemakera2iruntime</td></tr>
  <tr><td>Certificate Manager</td><td>certificatemanager</td><td>acm</td><td>acm</td><td>acm</td></tr>
  <tr><td>CloudControl API</td><td>cloudcontrolapi</td><td>cloudcontrolapi</td><td>cloudcontrol</td><td>cloudcontrol</td></tr>
  <tr><td>CloudSearch</td><td>cloudsearchv2</td><td>cloudsearch</td><td>cloudsearch</td><td>cloudsearch</td></tr>
  <tr><td>CloudSearch Domain</td><td>cloudsearchdomain</td><td>cloudsearch</td><td>cloudsearchdomain</td><td>cloudsearchdomain</td></tr>
  <tr><td>CloudWatch Events</td><td>cloudwatchevents</td><td>events</td><td>cloudwatchevents</td><td>cloudwatchevents</td></tr>
  <tr><td>CloudWatch Evidently</td><td>cloudwatchevidently</td><td>cloudwatchevidently</td><td>evidently</td><td>evidently</td></tr>
  <tr><td>CloudWatch Logs</td><td>logs</td><td>logs</td><td>cloudwatchlogs</td><td>cloudwatchlogs</td></tr>
  <tr><td>CloudWatch Metrics</td><td>metrics</td><td>cloudwatchmetrics</td><td>cloudwatch</td><td>cloudwatch</td></tr>
  <tr><td>CloudWatch Rum</td><td>cloudwatchrum</td><td>cloudwatchrum</td><td>rum</td><td>rum</td></tr>
  <tr><td>Cognito Identity Provider</td><td>cognitoidp</td><td>cognitoidp</td><td>cognitoidentityprovider</td><td>cognitoidentityprovider</td></tr>
  <tr><td>Connect Campaign</td><td>connectcampaign</td><td>connectcampaign</td><td>connectcampaigns</td><td>connectcampaigns</td></tr>
  <tr><td>Connect Wisdom</td><td>connectwisdom</td><td>connectwisdom</td><td>wisdom</td><td>wisdom</td></tr>
  <tr><td>Database Migration Service</td><td>databasemigrationservice</td><td>dms</td><td>databasemigration</td><td>databasemigration</td></tr>
  <tr><td>DataZone</td><td>datazone</td><td>datazoneexternal</td><td>datazone</td><td>datazone</td></tr>
  <tr><td>DynamoDB</td><td>dynamodbv2</td><td>dynamodb</td><td>dynamodb</td><td>dynamodb</td></tr>
  <tr><td>Elastic File System</td><td>elasticfilesystem</td><td>efs</td><td>efs</td><td>efs</td></tr>
  <tr><td>Elastic Map Reduce</td><td>elasticmapreduce</td><td>emr</td><td>emr</td><td>emr</td></tr>
  <tr><td>Glue DataBrew</td><td>gluedatabrew</td><td>gluedatabrew</td><td>databrew</td><td>databrew</td></tr>
  <tr><td>IAM Roles Anywhere</td><td>iamrolesanywhere</td><td>iamrolesanywhere</td><td>rolesanywhere</td><td>rolesanywhere</td></tr>
  <tr><td>Identity Management</td><td>identitymanagement</td><td>iam</td><td>iam</td><td>iam</td></tr>
  <tr><td>IoT Data</td><td>iotdata</td><td>iot</td><td>iotdataplane</td><td>iotdataplane</td></tr>
  <tr><td>Kinesis Analytics</td><td>kinesisanalytics</td><td>kinesis</td><td>kinesisanalytics</td><td>kinesisanalytics</td></tr>
  <tr><td>Kinesis Firehose</td><td>kinesisfirehose</td><td>kinesis</td><td>firehose</td><td>firehose</td></tr>
  <tr><td>Kinesis Video Signaling Channels</td><td>kinesisvideosignalingchannels</td><td>kinesisvideosignalingchannels</td><td>kinesisvideosignaling</td><td>kinesisvideosignaling</td></tr>
  <tr><td>Lex</td><td>lexruntime</td><td>lex</td><td>lexruntime</td><td>lexruntime</td></tr>
  <tr><td>Lookout For Vision</td><td>lookoutforvision</td><td>lookoutforvision</td><td>lookoutvision</td><td>lookoutvision</td></tr>
  <tr><td>Mainframe Modernization</td><td>mainframemodernization</td><td>mainframemodernization</td><td>m2</td><td>m2</td></tr>
  <tr><td>Marketplace Metering</td><td>marketplacemetering</td><td>marketplacemeteringservice</td><td>marketplacemetering</td><td>marketplacemetering</td></tr>
  <tr><td>Managed Grafana</td><td>managedgrafana</td><td>managedgrafana</td><td>grafana</td><td>grafana</td></tr>
  <tr><td>Mechanical Turk</td><td>mturk</td><td>mechanicalturkrequester</td><td>mturk</td><td>mturk</td></tr>
  <tr><td>Migration Hub Strategy Recommendations</td><td>migrationhubstrategyrecommendations</td><td>migrationhubstrategyrecommendations</td><td>migrationhubstrategy</td><td>migrationhubstrategy</td></tr>
  <tr><td>Nimble Studio</td><td>nimblestudio</td><td>nimblestudio</td><td>nimble</td><td>nimble</td></tr>
  <tr><td>Private 5G</td><td>private5g</td><td>private5g</td><td>privatenetworks</td><td>privatenetworks</td></tr>
  <tr><td>Prometheus</td><td>prometheus</td><td>prometheus</td><td>amp</td><td>amp</td></tr>
  <tr><td>Recycle Bin</td><td>recyclebin</td><td>recyclebin</td><td>rbin</td><td>rbin</td></tr>
  <tr><td>Redshift Data API</td><td>redshiftdataapi</td><td>redshiftdataapi</td><td>redshiftdata</td><td>redshiftdata</td></tr>
  <tr><td>Route 53</td><td>route53domains</td><td>route53</td><td>route53domains</td><td>route53domains</td></tr>
  <tr><td>Sage Maker Edge Manager</td><td>sagemakeredgemanager</td><td>sagemakeredgemanager</td><td>sagemakeredge</td><td>sagemakeredge</td></tr>
  <tr><td>Security Token</td><td>securitytoken</td><td>sts</td><td>sts</td><td>sts</td></tr>
  <tr><td>Server Migration</td><td>servermigration</td><td>servermigration</td><td>sms</td><td>sms</td></tr>
  <tr><td>Simple Email</td><td>simpleemail</td><td>ses</td><td>ses</td><td>ses</td></tr>
  <tr><td>Simple Email V2</td><td>simpleemailv2</td><td>sesv2</td><td>sesv2</td><td>sesv2</td></tr>
  <tr><td>Simple Systems Management</td><td>simplesystemsmanagement</td><td>ssm</td><td>ssm</td><td>ssm</td></tr>
  <tr><td>Simple Workflow</td><td>simpleworkflow</td><td>simpleworkflow</td><td>swf</td><td>swf</td></tr>
  <tr><td>Step Functions</td><td>stepfunctions</td><td>stepfunctions</td><td>sfn</td><td>sfn</td></tr>
</tbody>
</table>
