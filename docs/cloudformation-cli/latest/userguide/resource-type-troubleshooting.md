---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-troubleshooting.html
---

# Resource type development troubleshooting
<a name="resource-type-troubleshooting"></a>

This topic contains common issues regarding resource type development, and suggested solutions for those issues..

## Updates
<a name="resource-type-troubleshooting-updates"></a>
+ **Problem:** My service API implements Update actions as an Upsert, can I implement my CloudFormation resource type in this way?

  **Solution:** No, CloudFormation requires that `update` actions to a non-existing resource always throw a `ResourceNotFoundException`.

## Schema development
<a name="resource-type-troubleshooting-schema"></a>
+ **Problem:** How can I re-use existing schemas, or establish relationships to other resource types in my schema?

  **Solution:** Relationships and re-use are established using JSON Pointers. These are implemented using the `$ref` keyword in your resource type schema. Refer to [Modeling resource types to use with CloudFormation](resource-type-model.md) for more information.

## Permissions and authorization
<a name="resource-type-troubleshooting-permissions"></a>
+ **Problem:** Why am I getting an `AccessDeniedException` for my AWS API calls?

  **Solution:** If you are seeing errors in your logs related to AccessDeniedException for a Lambda Execution Role like:

  `A downstream service error occurred in a CREATE action on a AWS::MyService::MyResource: com.amazonaws.services.logs.model.AWSLogsException: User: arn:aws:sts::111122223333:assumed-role/UluruResourceHandlerLambdaExecutionRole-123456789012pdx/AWS-MYService-MyResource-Handler-1h344teffe is not authorized to perform: some:ApiCall on resource: some-resource (Service: AWSLogs; Status Code: 400; Error Code: AccessDeniedException; Request ID: 36af0cec-a96a-11e9-b204-ddabexample)`

  This is an indication that you are attempting to create and invoke AWS APIs using the default client, which is injected with environment credentials.

  For resource types, you should use the passed-in `AmazonWebServicesClientProxy` object to make AWS API calls, as in the following example.

  ```
  SesClient client = ClientBuilder.getClient();
  final CreateConfigurationSetRequest createConfigurationSetRequest =
      CreateConfigurationSetRequest.builder()
          .configurationSet(ConfigurationSet.builder()
              .name(model.getName())
              .build())
          .build();
  proxy.injectCredentialsAndInvokeV2(createConfigurationSetRequest, client::createConfigurationSet);
  ```
+ **Problem:** How do I specify credentials for non-AWS API calls?

  **Solution:** For non-AWS API calls which require authentication and authorization, you should create properties in your resource type which contain the credentials. Define these properties in the resource type schema as `writeOnlyProperties`.

  Users can then provide their own credentials through their CloudFormation templates. We encourage the use of [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) in CloudFormation templates, which can use AWS Secrets Manager to fetch credentials at runtime.

## Resource type development
<a name="resource-type-troubleshooting-dev"></a>
+ **Problem:** Can I share functionality between resource by adding common functionality to the `BaseHandler`?

  **Solution:** Because the `BaseHandler` is code-generated, it cannot be edited.
+ **Problem:** For Java development, is there a way to include multiple resources in a single maven project?

  **Solution:** Not currently. For security and manageability, the CloudFormation Registry registers each resource type as a separate, versioned, type. You could still share code through a shared package. Ideally, the wrapper layer does most of the boilerplate. If you see a need for more boilerplate, we would like to know how we can improve for that use case rather than combine types in a package, so please reach out to the team.
+ **Problem:** Will `software.amazon.cloudformation.proxy.Logger` have debug/info/warning/error levels/?

  **Solution:** Currently, all log messages are emitted to CloudWatch, which has no built-in concept of log levels.
+ **Problem:** Does CloudFormation have a sandbox environment I can use to test and experiment with my extensions?

  **Solution:** Using extensions from your private registry in stacks created in your account is the same as using a sandbox environment.

## Testing
<a name="resource-type-troubleshooting-test"></a>
+ **Problem:** For testing, when should I use `sam local invoke`, `cfn test` and `mvn test`?

  **Solution:** Use the various test capabilities for the test scenarios described below.
  + `sam local invoke`: Creating custom integration test by passing in custom CloudFormation payloads and isolate specific handlers.
  + `cfn test`: Contract tests meant to cycle through CRUDL actions and ideally leave in a clean state (if tests pass).
  + `mvn test`: Used for Unit testing. The goal is to confirm that each method or unit of the resource performs as intended. It also helps to ensure that you have enough code coverage. We expect unit tests to mock dependencies and not create real resources.
+ **Problem:** How do I get the latest changes for a contract test?

  **Solution:** Run `pip install cloudformation-cli cloudformation-cli-<language>-plugin --upgrade`.
+ **Problem:** Where can I find the code for contract tests?

  **Solution:** You can find the code for the test suite at [https://github.com/aws-cloudformation/cloudformation-cli/tree/master/src/rpdk/core/contract/suite](https://github.com/aws-cloudformation/cloudformation-cli/tree/master/src/rpdk/core/contract/suite).
+ **Problem:** How do I check which version of contract tests I’m running?

  **Solution:** Run `pip freeze`. The output shows the CloudFormation CLI version. The list of all releases for the CloudFormation CLI can be found at [https://github.com/aws-cloudformation/cloudformation-cli/releases](https://github.com/aws-cloudformation/cloudformation-cli/releases).
+ **Problem:** I found a bug in the contract tests. How do I report it?

  **Solution:** File an issue at [https://github.com/aws-cloudformation/cloudformation-cli/issues](https://github.com/aws-cloudformation/cloudformation-cli/issues).
+ **Problem:** How can I contribute to the development of contract tests?

  **Solution:** Follow [these steps](https://github.com/aws-cloudformation/cloudformation-cli#development) to install a virtual development environment on your local machine.
+ **Problem:** Contract tests time out on my local machine. How do I resolve this issue?

  **Solution:** Contract tests assert that `create`, `update`, and `delete` handlers return progress events every 60 seconds, and that `read` and `list` handlers complete in 30 seconds. If you see errors for tests timing out, you can increase the timeout by running contract tests with the following argument: `cfn test --enforce-timeout <value>`. The value specified is the new timeout threshold for the `read` and `list` handlers. The new threshold for the `create`, `update`, and `delete` handlers is double the value specified.
+ **Problem:** How do I run one contract test at a time?

  **Solution:** You can run one contract test by running the following command: `cfn test -- -k <test-name>`.
+ **Problem:** How do I define input files for contract tests?

  **Solution:** [Specifying input data for use in contract tests](resource-type-test.md#resource-type-test-input-data) describes how to pass an input for contract tests and what each file should contain.
+ **Problem:** How do I fix the `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` error?

  **Solution:** This exception message indicates that you might be running out of memory or time. Add the following lines under `Globals` in the `template.yaml` file in your code package.

  ```
  Globals:
    Function:
      Timeout: 180
      MemorySize: 256
  ```
+ **Problem:** Why do create operations fail when the `primaryIdentifier` is null?

  **Solution:** The `create` handler should return the `primaryIdentifier` in the model. If the `primaryIdentifier` for your resource is a read-only property, you can update the returned model with the property or invoke the `read` handler in your `create` handler.
+ **Problem:** Some tests fail because the input is not equal to the output. How do I fix this?

  **Solution:** Input-output comparisons check that all properties are exactly equal, except for read-only properties, write-only properties, defaults, `insertionOrder`, and `uniqueItems`.
+ **Problem:** Can the `update` handler update create-only properties?

  **Solution:** No. The `update` handler cannot update create-only properties. These properties should remain the same in `update` models.
+ **Problem:** Why does my `delete`/`read` handler fail with a `NotFound` or `InvalidRequest` error code?

  **Solution:** Ensure that your input to these handlers is correct. The `delete` and `read` handlers should be successfully invoked with just the `primaryIdentifier`. The `read` handler can also be invoked with `additionalIdentifiers`.
+ **Problem:** Why do delete operations fail when `resourceModel` isn't null?

  **Solution:** The `delete` handler shouldn't return a model when successful. You need to redact the model from the returned progress event.
+ **Problem:** All of my properties are marked as create-only properties. Why do the `update` contract tests keep running and failing?

  **Solution:** Remove the `update` block from the `handlers` section in your schema file.
+ **Problem:** How do I fix permission issues during test execution?

  **Solution:** Check the exception message to see which permissions are missing. Add these permissions to `ExecutionRole` in the `resource-role.yaml` file in your code package.

## Deployment
<a name="resource-type-troubleshooting-deploy"></a>
+ **Problem:** Is the resource type interface guaranteed to be stable?

  **Solution:** The communication protocol between CloudFormation and your resource type package is subject to change. However this will be done in a backwards-compatible way, using versioned interfaces. This will be invisible to you as a developer and is managed as part of the CloudFormation managed platform.

  The interface that your handlers implement inside your package is expected to be stable. We may introduce improvements, such as security fixes or other changes to the package, but these will be done with versioned dependency or CloudFormation CLI updates. You aren't required to upgrade your packages to publish them, only to incorporate these improvements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
