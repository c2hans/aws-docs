---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/runtime-update.html
---

# Updating Lambda runtimes for resource types and hooks
<a name="runtime-update"></a>

AWS CloudFormation resource types and hooks are developed using CloudFormation CLI language plug-ins available for Go, Java, Python, and TypeScript. The language plug-ins eventually need to be updated in order to maintain compatibility.

You can update your runtime by modifying parameters in the `.rpdk-config` and `template.yml` files. These files are found in your resource provider or hooks package. We recommend that your CloudFormation resource types and hooks use supported [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).

## Upgrading the Java runtime
<a name="java-upgrade"></a>

**Steps to upgrade to Java 17**Upgrade to Java 17

1. In the `.rpdk-config` file, change the `runtime` parameter to `java17`.

   The following is an example `.rpdk-config` using the `java17` runtime:

   ```
   {
       "typeName": "AWS::DirectoryService::SimpleAD",
       "language": "java",
       "runtime": "java17",
       "entrypoint": "software.amazon.directoryservice.simplead.HandlerWrapper::handleRequest",
       "testEntrypoint": "software.amazon.directoryservice.simplead.HandlerWrapper::testEntrypoint",
       "settings": {
           "namespace": [
               "software",
               "amazon",
               "directoryservice",
               "simplead"
           ],
           "protocolVersion": "2.0.0"
       }
   }
   ```

1. In the `template.yml` file:
   + In `TypeFunction` and `TestEntrypoint`, change the `Runtime` parameters to `java17`.

   The following is an example `template.yml` file using the `java17` runtime:

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Transform: AWS::Serverless-2016-10-31
   Description: AWS SAM template for the AWS::DirectoryService::SimpleAD resource type

   Globals:
     Function:
       Timeout: 180  # docker start-up times can be long for SAM CLI
       MemorySize: 1024

   Resources:
     TypeFunction:
       Type: AWS::Serverless::Function
       Properties:
         Handler: software.amazon.directoryservice.simplead.HandlerWrapper::handleRequest
         Runtime: java17
         CodeUri: ./target/aws-directoryservice-simplead-handler-1.0-SNAPSHOT.jar

     TestEntrypoint:
       Type: AWS::Serverless::Function
       Properties:
         Handler: software.amazon.directoryservice.simplead.HandlerWrapper::testEntrypoint
         Runtime: java17
         CodeUri: ./target/aws-directoryservice-simplead-handler-1.0-SNAPSHOT.jar
   ```

## Upgrading the Go runtime
<a name="os-only-runtime-upgrade"></a>

**Steps to upgrade to provided.al2**Upgrade to provided.al2

1. In the `.rpdk-config` file:
   + Change the `runtime` parameter to `porovided.al2`.
   + Change `entrypoint` and `testEntrypoint` paramters to `bootstrap`.

   The following is an example `.rpdk-config` file using the `provided.al2` runtime:

   ```
   {
       "typeName": "Example::GitHub::Repo",
       "language": "go",
       "runtime": "provided.al2",
       "entrypoint": "bootstrap",
       "testEntrypoint": "bootstrap",
       "settings": {
           "import_path": "github.com/aws-cloudformation/cloudformation-cli-go-plugin/examples/github-repo",
           "protocolVersion": "2.0.0",
           "pluginVersion": "2.0.0"
       }
   }
   ```

1. In the template.yml file:
   + In `TypeFunction` and `TestEntrypoint`, change the `Runtime` parameters to `provided.al2`.
   + In `TypeFunction` and `TestEntrypoint`, change the `Handler` parameters to `bootstrap`.
   + In `TypeFunction` and `TestEntrypoint`, add `x86_64` to the `Architecture` parameter.

   The following is an example `template.yml` file using the `provided.al2` runtime:

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Transform: AWS::Serverless-2016-10-31
   Description: AWS SAM template for the Example::GitHub::Repo resource type

   Globals:
     Function:
       Timeout: 60  # docker start-up times can be long for SAM CLI

   Resources:
     TypeFunction:
       Type: AWS::Serverless::Function
       Metadata:
         BuildMethod: go1.x
       Properties:
         Handler: bootstrap
         Runtime: provided.al2
         Architectures:
           - x86_64
         CodeUri: bin/
         # Uncomment to test with AWS resources
         # Environment:
         #   Variables:
         #     AWS_FORCE_INTEGRATIONS: "true"

     TestEntrypoint:
       Type: AWS::Serverless::Function
       Metadata:
         BuildMethod: go1.x
       Properties:
         Handler: bootstrap
         Runtime: provided.al2
         Architectures:
           - x86_64
         CodeUri: bin/
   ```

## Upgrading the Python runtime
<a name="python-runtime-upgrade"></a>

**Steps to upgrade to Python 3.11**Upgrade to Python 3.11

1. In the `.rpdk-config` file:
   + Change the `runtime` parameter to `python3.11`.
   + Change the `language` parameter to `python311`.

   The following is an example `.rpdk-config` file using the `python3.11` runtime:

   ```
   {
       "artifact_type": "RESOURCE",
       "typeName": "AWS::EC2::Instance",
       "language": "python311",
       "runtime": "python3.11",
       "entrypoint": "aws_ec2_instance.handlers.resource",
       "testEntrypoint": "aws_ec2_instance.handlers.test_entrypoint",
       "settings": {
           "version": false,
           "subparser_name": null,
           "verbose": 0,
           "force": false,
           "type_name": null,
           "artifact_type": null,
           "endpoint_url": null,
           "region": null,
           "target_schemas": [],
           "profile": null,
           "use_docker": true,
           "no_docker": false,
           "protocolVersion": "2.0.0"
       }
   }
   ```

1. In the `template.yml` file:
   + In `TypeFunction` and `TestEntrypoint`, change the `Runtime` parameters to `python3.11`.

   The following is an example `template.yml` file using the `python3.11` runtime:

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Transform: AWS::Serverless-2016-10-31
   Description: AWS SAM template for the AWS::EC2::Instance resource type

   Globals:
     Function:
       Timeout: 180  # docker start-up times can be long for SAM CLI
       MemorySize: 256

   Resources:
     TypeFunction:
       Type: AWS::Serverless::Function
       Properties:
         Handler: aws_ec2_instance.handlers.resource
         Runtime: python3.11
         CodeUri: build/

     TestEntrypoint:
       Type: AWS::Serverless::Function
       Properties:
         Handler: aws_ec2_instance.handlers.test_entrypoint
         Runtime: python3.11
         CodeUri: build/
   ```

## Upgrading the Node.js runtime
<a name="node-js-runtime-upgrade"></a>

**Steps to upgrade to Node.js 18**Upgrade to Node.js 18

1. In the `.rpdk-config` file, change the `runtime` parameter to `nodejs18.x`.

   ```
   {
       "artifact_type": "RESOURCE",
       "typeName": "Dynatrace::Environment::Metric",
       "language": "typescript",
       "runtime": "nodejs18.x",
       "entrypoint": "dist/Dynatrace-Environment-Metric/src/handlers.entrypoint",
       "testEntrypoint": "dist/Dynatrace-Environment-Metric/src/handlers.testEntrypoint",
       "settings": {
           "version": false,
           "subparser_name": null,
           "verbose": 0,
           "force": false,
           "type_name": null,
           "artifact_type": null,
           "endpoint_url": null,
           "region": null,
           "target_schemas": [],
           "useDocker": false,
           "protocolVersion": "2.0.0"
       },
       "contractSettings":{
           "typeConfiguration": {
               "configuration": {
                   "DynatraceAccess": {
                       "Token": "{{resolve:ssm-secure:/cfn/dynatrace/token:1}}",
                       "Endpoint": "{{resolve:ssm-secure:/cfn/dynatrace/endpoint:1}}"
                   }
               },
               "configurationAlias": "default"
           }
       }
   }
   ```

1. In the `template.yml` file:
   + In `TestEntrypoint` and `TypeFunction`, change the `Runtime` parameters to `nodejs18.x`.

   The following is an example `template.yml` file using the `nodejs18.x` runtime:

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Transform: AWS::Serverless-2016-10-31
   Description: AWS SAM template for the Dynatrace::Environment::Metric resource type

   Globals:
     Function:
       Timeout: 180  # docker start-up times can be long for SAM CLI
       MemorySize: 256

   Resources:
     TestEntrypoint:
       Type: AWS::Serverless::Function
       Properties:
         Handler: dist/Dynatrace-Environment-Metric/src/handlers.testEntrypoint
         Runtime: nodejs18.x
         CodeUri: ./

     TypeFunction:
       Type: AWS::Serverless::Function
       Properties:
         Handler: dist/Dynatrace-Environment-Metric/src/handlers.entrypoint
         Runtime: nodejs18.x
         CodeUri: ./
   ```
