---
source_url: https://docs.aws.amazon.com/marketplace/latest/developerguide/logging-deployment-api-calls-with-cloudtrail.html
---

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Logging AWS Marketplace Deployment API calls with CloudTrail

The AWS Marketplace Deployment Service is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures calls to the Deployment API operations as events. These include calls that publish deployment parameters and calls that start and read deployment configuration jobs. For more information, see [Deployment Service management events in CloudTrail](#deployment-information-in-cloudtrail).

With the information that CloudTrail collects, you can determine the request that was made to the Deployment Service, the IP address it came from, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The **Event history** provides a record of the past 90 days of management events in an AWS Region. This record is viewable, searchable, downloadable, and immutable. For more information, see [Working with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## Deployment Service management events in CloudTrail
<a name="deployment-information-in-cloudtrail"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

The AWS Marketplace Deployment Service logs the following Deployment API operations to CloudTrail as management events. The event source is `deployment-marketplace.amazonaws.com`. The `readOnly` column shows the value of the `readOnly` field in each event, which you can use to filter events in a trail or event data store.

| Operation | `readOnly` |
| --- | --- |
| [GetDeploymentConfiguration](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_GetDeploymentConfiguration.html) | true |
| [GetDeploymentConfigurationJob](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_GetDeploymentConfigurationJob.html) | true |
| [ListDeploymentConfigurationJobs](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_ListDeploymentConfigurationJobs.html) | true |
| [ListTagsForResource](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_ListTagsForResource.html) | true |
| [PutDeploymentParameter](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_PutDeploymentParameter.html) | false |
| [StartDeploymentConfigurationJob](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_StartDeploymentConfigurationJob.html) | false |
| [TagResource](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_TagResource.html) | false |
| [UntagResource](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_UntagResource.html) | false |

## Deployment Service event examples
<a name="deployment-understanding-log-entries"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following JSON example shows a CloudTrail event that demonstrates the `PutDeploymentParameter` operation:

```json
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudTrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP123"
    },
    "eventTime": "2023-11-16T16:32:48Z",
    "eventSource": "deployment-marketplace.amazonaws.com",
    "eventName": "PutDeploymentParameter",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-sdk-java/2.20.162 Mac_OS_X/13.5.2 OpenJDK_64-Bit_Server_VM/18.0.1+10-FR Java/18.0.1 vendor/Amazon.com_Inc. io/sync http/UrlConnection cfg/retry-mode/legacy",
    "requestParameters": {
        "productId": "prod-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "catalog": "AWSMarketplace",
        "clientToken": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "agreementId": "agmt-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "deploymentParameter": {
            "name": "PutDeploymentParameterCloudTrailTest-secret",
            "secretString": "***"
        },
        "expirationDate": "2023-11-30T03:02:26.779241Z"
    },
    "responseElements": {
        "agreementId": "agmt-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "deploymentParametersId": "dp-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "resourceArn": "arn:aws:aws-marketplace:us-east-1:123456789010:DeploymentParameter:catalogs/AWSMarketplace/products/prod-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1/dp-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1"
    },
    "requestID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
    "eventID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789010",
    "eventCategory": "Management"
}
```

The following JSON example shows a CloudTrail event that demonstrates the `StartDeploymentConfigurationJob` operation:

```json
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA123456789EXAMPLE:ExampleSession",
        "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleSession",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA123456789EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/ExampleRole",
                "accountId": "111122223333",
                "userName": "ExampleRole"
            },
            "attributes": {
                "creationDate": "2026-11-19T21:18:19Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2026-11-19T21:20:31Z",
    "eventSource": "deployment-marketplace.amazonaws.com",
    "eventName": "StartDeploymentConfigurationJob",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-cli/2.31.0 Python/3.13.7 Linux/6.1.0 exe/x86_64.amzn.2023",
    "requestParameters": {
        "catalog": "AWSMarketplace",
        "productId": "prod-EXAMPLEa1b2c3",
        "deliveryOptionType": "data-as-a-service",
        "configuration": {
            "dataAsAService": {
                "fulfillmentUrl": "https://example.com/register"
            }
        },
        "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "tags": {
            "Team": "Data"
        }
    },
    "responseElements": {
        "jobId": "a1b2c3d4567890abcdef0123456789ab",
        "status": "IN_PROGRESS",
        "configuration": {
            "dataAsAService": {
                "fulfillmentUrl": "https://example.com/register"
            }
        },
        "createdAt": "2026-11-19T21:20:31.073529832Z"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::Marketplace::DeploymentConfiguration",
            "ARN": "arn:aws:aws-marketplace:us-east-1:111122223333:DeploymentConfiguration:catalogs/AWSMarketplace/products/prod-EXAMPLEa1b2c3/delivery-options/data-as-a-service"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail record contents for management, data, and network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.
