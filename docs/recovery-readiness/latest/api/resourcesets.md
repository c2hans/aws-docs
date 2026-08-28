---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html
---

# ListResourceSets, CreateResourceSet
<a name="resourcesets"></a>

## URI
<a name="resourcesets-url"></a>

`/resourcesets`

## HTTP methods
<a name="resourcesets-http-methods"></a>

### GET
<a name="resourcesetsget"></a>

**Operation ID:** `ListResourceSets`

Lists the resource sets in an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListResourceSetsResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="resourcesetspost"></a>

**Operation ID:** `CreateResourceSet`

Creates a resource set. A resource set is a set of resources of one type that span multiple cells. You can associate a resource set with a readiness check to monitor the resources for failover readiness.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ResourceSetOutput | 200 response |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 409 | None | 409 response - Conflict exception. You might be using a predefined variable. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="resourcesetsoptions"></a>

Enable CORS by returning correct headers

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="resourcesets-schemas"></a>

### Request bodies
<a name="resourcesets-request-examples"></a>

#### POST schema
<a name="resourcesets-request-body-post-example"></a>

```
{
  "resourceSetType": "string",
  "resourceSetName": "string",
  "resources": [
    {
      "readinessScopes": [
        "string"
      ],
      "componentId": "string",
      "resourceArn": "string",
      "dnsTargetResource": {
        "recordType": "string",
        "domainName": "string",
        "hostedZoneArn": "string",
        "targetResource": {
          "r53Resource": {
            "domainName": "string",
            "recordSetId": "string"
          },
          "nLBResource": {
            "arn": "string"
          }
        },
        "recordSetId": "string"
      }
    }
  ],
  "tags": {
  }
}
```

### Response bodies
<a name="resourcesets-response-examples"></a>

#### ListResourceSetsResult schema
<a name="resourcesets-response-body-listresourcesetsresult-example"></a>

```
{
  "nextToken": "string",
  "resourceSets": [
    {
      "resourceSetType": "string",
      "resourceSetName": "string",
      "resources": [
        {
          "readinessScopes": [
            "string"
          ],
          "componentId": "string",
          "resourceArn": "string",
          "dnsTargetResource": {
            "recordType": "string",
            "domainName": "string",
            "hostedZoneArn": "string",
            "targetResource": {
              "r53Resource": {
                "domainName": "string",
                "recordSetId": "string"
              },
              "nLBResource": {
                "arn": "string"
              }
            },
            "recordSetId": "string"
          }
        }
      ],
      "resourceSetArn": "string",
      "tags": {
      }
    }
  ]
}
```

#### ResourceSetOutput schema
<a name="resourcesets-response-body-resourcesetoutput-example"></a>

```
{
  "resourceSetType": "string",
  "resourceSetName": "string",
  "resources": [
    {
      "readinessScopes": [
        "string"
      ],
      "componentId": "string",
      "resourceArn": "string",
      "dnsTargetResource": {
        "recordType": "string",
        "domainName": "string",
        "hostedZoneArn": "string",
        "targetResource": {
          "r53Resource": {
            "domainName": "string",
            "recordSetId": "string"
          },
          "nLBResource": {
            "arn": "string"
          }
        },
        "recordSetId": "string"
      }
    }
  ],
  "resourceSetArn": "string",
  "tags": {
  }
}
```

## Properties
<a name="resourcesets-properties"></a>

### DNSTargetResource
<a name="resourcesets-model-dnstargetresource"></a>

A component for DNS/routing control readiness checks and architecture checks.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | False | The domain name that acts as an ingress point to a portion of the customer application. |
| hostedZoneArn | string | False | The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource. |
| recordSetId | string | False | The Route 53 record set ID that uniquely identifies a DNS record, given a name and a type. |
| recordType | string | False | The type of DNS record of the target resource. |
| targetResource | [TargetResource](#resourcesets-model-targetresource) | False | The target resource of the DNS target resource. |

### ListResourceSetsResult
<a name="resourcesets-model-listresourcesetsresult"></a>

The result of a successful `ListResourceSets` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The token that identifies which batch of results you want to see. |
| resourceSets | Array of type [ResourceSetOutput](#resourcesets-model-resourcesetoutput) | False | A list of resource sets associated with the account. |

### NLBResource
<a name="resourcesets-model-nlbresource"></a>

The Network Load Balancer resource that a DNS target resource points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Network Load Balancer resource Amazon Resource Name (ARN). |

### R53ResourceRecord
<a name="resourcesets-model-r53resourcerecord"></a>

The Route 53 resource that a DNS target resource record points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | False | The DNS target domain name. |
| recordSetId | string | False | The Route 53 Resource Record Set ID. |

### Resource
<a name="resourcesets-model-resource"></a>

The resource element of a resource set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| componentId | string | False | The component identifier of the resource, generated when DNS target resource is used. |
| dnsTargetResource | [DNSTargetResource](#resourcesets-model-dnstargetresource) | False | The DNS target resource. |
| readinessScopes | Array of type string | False | The recovery group Amazon Resource Name (ARN) or the cell ARN that the readiness checks for this resource set are scoped to. |
| resourceArn | string | False | The Amazon Resource Name (ARN) of the AWS resource. |

### ResourceSetCreateParameters
<a name="resourcesets-model-resourcesetcreateparameters"></a>

The parameters used to create a resource set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resources | Array of type [Resource](#resourcesets-model-resource) | True | A list of resource objects in the resource set. |
| resourceSetName | string | True | The name of the resource set to create. |
| resourceSetType | string<br />Pattern: `AWS::[A-Za-z0-9]+::[A-Za-z0-9]+` | True | The resource type of the resources in the resource set. One of the following values:<br />AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource |
| tags | [Tags](#resourcesets-model-tags) | False | A tag to associate with the parameters for a resource set. |

### ResourceSetOutput
<a name="resourcesets-model-resourcesetoutput"></a>

A collection of resources of the same type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resources | Array of type [Resource](#resourcesets-model-resource) | True | A list of resource objects. |
| resourceSetArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the resource set. |
| resourceSetName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the resource set. |
| resourceSetType | string<br />Pattern: `AWS::[A-Za-z0-9]+::[A-Za-z0-9]+` | True | The resource type of the resources in the resource set. One of the following values:<br />AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource |
| tags | [Tags](#resourcesets-model-tags) | False |  |

### Tags
<a name="resourcesets-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TargetResource
<a name="resourcesets-model-targetresource"></a>

The target resource that the Route 53 record points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nLBResource | [NLBResource](#resourcesets-model-nlbresource) | False | The Network Load Balancer resource. |
| r53Resource | [R53ResourceRecord](#resourcesets-model-r53resourcerecord) | False | The Route 53 resource. |

## See also
<a name="resourcesets-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListResourceSets
<a name="ListResourceSets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/ListResourceSets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListResourceSets)

### CreateResourceSet
<a name="CreateResourceSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/CreateResourceSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/CreateResourceSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
