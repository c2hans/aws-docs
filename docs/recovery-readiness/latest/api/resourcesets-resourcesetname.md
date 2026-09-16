---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html
---

# GetResourceSet, UpdateResourceSet, DeleteResourceSet
<a name="resourcesets-resourcesetname"></a>

## URI
<a name="resourcesets-resourcesetname-url"></a>

`/resourcesets/{{resourceSetName}}`

## HTTP methods
<a name="resourcesets-resourcesetname-http-methods"></a>

### GET
<a name="resourcesets-resourcesetnameget"></a>

**Operation ID:** `GetResourceSet`

Displays the details about a resource set, including a list of the resources in the set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceSetName}} | String | True | Name of a resource set. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ResourceSetOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### PUT
<a name="resourcesets-resourcesetnameput"></a>

**Operation ID:** `UpdateResourceSet`

Updates a resource set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceSetName}} | String | True | Name of a resource set. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ResourceSetOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### DELETE
<a name="resourcesets-resourcesetnamedelete"></a>

**Operation ID:** `DeleteResourceSet`

Deletes a resource set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceSetName}} | String | True | Name of a resource set. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="resourcesets-resourcesetnameoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceSetName}} | String | True | Name of a resource set. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="resourcesets-resourcesetname-schemas"></a>

### Request bodies
<a name="resourcesets-resourcesetname-request-examples"></a>

#### PUT schema
<a name="resourcesets-resourcesetname-request-body-put-example"></a>

```
{
  "resourceSetType": "string",
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
  ]
}
```

### Response bodies
<a name="resourcesets-resourcesetname-response-examples"></a>

#### ResourceSetOutput schema
<a name="resourcesets-resourcesetname-response-body-resourcesetoutput-example"></a>

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
<a name="resourcesets-resourcesetname-properties"></a>

### DNSTargetResource
<a name="resourcesets-resourcesetname-model-dnstargetresource"></a>

A component for DNS/routing control readiness checks and architecture checks.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | False | The domain name that acts as an ingress point to a portion of the customer application. |
| hostedZoneArn | string | False | The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource. |
| recordSetId | string | False | The Route 53 record set ID that uniquely identifies a DNS record, given a name and a type. |
| recordType | string | False | The type of DNS record of the target resource. |
| targetResource | [TargetResource](#resourcesets-resourcesetname-model-targetresource) | False | The target resource of the DNS target resource. |

### NLBResource
<a name="resourcesets-resourcesetname-model-nlbresource"></a>

The Network Load Balancer resource that a DNS target resource points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Network Load Balancer resource Amazon Resource Name (ARN). |

### R53ResourceRecord
<a name="resourcesets-resourcesetname-model-r53resourcerecord"></a>

The Route 53 resource that a DNS target resource record points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | False | The DNS target domain name. |
| recordSetId | string | False | The Route 53 Resource Record Set ID. |

### Resource
<a name="resourcesets-resourcesetname-model-resource"></a>

The resource element of a resource set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| componentId | string | False | The component identifier of the resource, generated when DNS target resource is used. |
| dnsTargetResource | [DNSTargetResource](#resourcesets-resourcesetname-model-dnstargetresource) | False | The DNS target resource. |
| readinessScopes | Array of type string | False | The recovery group Amazon Resource Name (ARN) or the cell ARN that the readiness checks for this resource set are scoped to. |
| resourceArn | string | False | The Amazon Resource Name (ARN) of the AWS resource. |

### ResourceSetOutput
<a name="resourcesets-resourcesetname-model-resourcesetoutput"></a>

A collection of resources of the same type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resources | Array of type [Resource](#resourcesets-resourcesetname-model-resource) | True | A list of resource objects. |
| resourceSetArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the resource set. |
| resourceSetName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the resource set. |
| resourceSetType | string<br />Pattern: `AWS::[A-Za-z0-9]+::[A-Za-z0-9]+` | True | The resource type of the resources in the resource set. One of the following values:<br />AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource |
| tags | [Tags](#resourcesets-resourcesetname-model-tags) | False |  |

### ResourceSetUpdateParameters
<a name="resourcesets-resourcesetname-model-resourcesetupdateparameters"></a>

Parameters used to create a resource set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resources | Array of type [Resource](#resourcesets-resourcesetname-model-resource) | True | A list of resource objects. |
| resourceSetType | string<br />Pattern: `AWS::[A-Za-z0-9]+::[A-Za-z0-9]+` | True | The resource type of the resources in the resource set. One of the following values:<br />AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource |

### Tags
<a name="resourcesets-resourcesetname-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TargetResource
<a name="resourcesets-resourcesetname-model-targetresource"></a>

The target resource that the Route 53 record points to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nLBResource | [NLBResource](#resourcesets-resourcesetname-model-nlbresource) | False | The Network Load Balancer resource. |
| r53Resource | [R53ResourceRecord](#resourcesets-resourcesetname-model-r53resourcerecord) | False | The Route 53 resource. |

## See also
<a name="resourcesets-resourcesetname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetResourceSet
<a name="GetResourceSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/GetResourceSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetResourceSet)

### UpdateResourceSet
<a name="UpdateResourceSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/UpdateResourceSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/UpdateResourceSet)

### DeleteResourceSet
<a name="DeleteResourceSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/DeleteResourceSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/DeleteResourceSet)
