---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 The Dynamic Object and Rule Extensions for AWS Network Firewall solution has a two-tier architecture, which consists of the business tier and data tier. The business tier is powered by a combination of [Amazon API Gateway](https://aws.amazon.com/api-gateway/) and [AWS Lambda](https://aws.amazon.com/lambda/). The business logic predominantly resides in AWS Lambda for managing the domain data and periodically running a Lambda function to keep data synchronized between the solution and ANFW instance. The data tier is underpinned by [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to store rule bundle, object, and rule data.

 The architecture can be grouped into two logical components:
+  Request orchestration
+  Automatic resource and rule synchronization, and ANFW configuration

![Dynamic Object and Rule Extensions for AWS Network Firewall architecture](http://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/images/dynamic-object-and-rule-extensions-for-aws-network-firewall-architecture.png)

1.  The API Gateway provides the primary interface for the user to interact with this solution, including endpoints to manage the domain entities. Domain entities include rule, object, rule bundle, and list audit information. Refer to [API schema](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/) in the GitHub repository for sample requests and information about updating the metadata.

1.  The request is forwarded to a Lambda handler function.

1.  (Optional) When `enableOpa` = `true`, a Lambda function invokes ECS-hosted OPA cluster to exercise validation on the request based on context. For example, Lambda function can validate if the requester is allowed to perform the `CreateObject` action.

1.  Lambda issues request data to read from or write to domain entity tables in DynamoDB.

1.  An [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule is scheduled to invoke the Auto Config Lambda function. The frequency is based on the `ruleResolutionInterval` configuration; the default value is 10 minutes.

1.  The auto config Lambda function requests domain entity data such as rule bundle, rule, and object from Amazon DynamoDB.

1.  The auto config Lambda function queries the [AWS Config](https://aws.amazon.com/config/) [aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) to resolve defined object referenced by rule in the solution.

1.  The auto Config Lambda function sends an update request to ANFW.
