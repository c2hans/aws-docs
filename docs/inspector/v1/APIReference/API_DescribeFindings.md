---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeFindings.html
---

# DescribeFindings
<a name="API_DescribeFindings"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the findings that are specified by the ARNs of the findings.

## Request Syntax
<a name="API_DescribeFindings_RequestSyntax"></a>

```
{
   "findingArns": [ "{{string}}" ],
   "locale": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFindings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [findingArns](#API_DescribeFindings_RequestSyntax) **   <a name="Inspector-DescribeFindings-request-findingArns"></a>
The ARN that specifies the finding that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [locale](#API_DescribeFindings_RequestSyntax) **   <a name="Inspector-DescribeFindings-request-locale"></a>
The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.
Type: String
Valid Values: `EN_US`
Required: No

## Response Syntax
<a name="API_DescribeFindings_ResponseSyntax"></a>

```
{
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   },
   "findings": [
      {
         "arn": "string",
         "assetAttributes": {
            "agentId": "string",
            "amiId": "string",
            "autoScalingGroup": "string",
            "hostname": "string",
            "ipv4Addresses": [ "string" ],
            "networkInterfaces": [
               {
                  "ipv6Addresses": [ "string" ],
                  "networkInterfaceId": "string",
                  "privateDnsName": "string",
                  "privateIpAddress": "string",
                  "privateIpAddresses": [
                     {
                        "privateDnsName": "string",
                        "privateIpAddress": "string"
                     }
                  ],
                  "publicDnsName": "string",
                  "publicIp": "string",
                  "securityGroups": [
                     {
                        "groupId": "string",
                        "groupName": "string"
                     }
                  ],
                  "subnetId": "string",
                  "vpcId": "string"
               }
            ],
            "schemaVersion": number,
            "tags": [
               {
                  "key": "string",
                  "value": "string"
               }
            ]
         },
         "assetType": "string",
         "attributes": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "confidence": number,
         "createdAt": number,
         "description": "string",
         "id": "string",
         "indicatorOfCompromise": boolean,
         "numericSeverity": number,
         "recommendation": "string",
         "schemaVersion": number,
         "service": "string",
         "serviceAttributes": {
            "assessmentRunArn": "string",
            "rulesPackageArn": "string",
            "schemaVersion": number
         },
         "severity": "string",
         "title": "string",
         "updatedAt": number,
         "userAttributes": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedItems](#API_DescribeFindings_ResponseSyntax) **   <a name="Inspector-DescribeFindings-response-failedItems"></a>
Finding details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [findings](#API_DescribeFindings_ResponseSyntax) **   <a name="Inspector-DescribeFindings-response-findings"></a>
Information about the finding.
Type: Array of [Finding](API_Finding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_DescribeFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_DescribeFindings_Examples"></a>

### Example
<a name="API_DescribeFindings_Example_1"></a>

This example illustrates one usage of DescribeFindings.

#### Sample Request
<a name="API_DescribeFindings_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 133
               X-Amz-Target: InspectorService.DescribeFindings
               X-Amz-Date: 20160323T215809Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "findingArns": [
                   "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4"
                 ]
               }
```

#### Sample Response
<a name="API_DescribeFindings_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: 555dbc27-f142-11e5-9dc2-6746fe4b2002
               Content-Type: application/x-amz-json-1.1
               Content-Length: 892
               Date: Wed, 23 Mar 2016 21:58:10 GMT
               {
                 "failedItems": {},
                 "findings": [
                   {
                     "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4",
                      "assetAttributes": {
                        "agentId": "i-092e1184e67721f24",
                        "amiId": "ami-0ad99772",
                        "autoScalingGroup": "auto scaling group",
                        "hostname": "ec2-54-202-242-173.us-west-2.compute.amazonaws.com",
                        "ipv4Addresses": [],
                        "networkInterfaces": [
                          {
                            "ipv6Addresses": [],
                            "networkInterfaceId": "eni-09b5ad02",
                            "privateDnsName": "ip-172-31-36-75.us-west-2.compute.internal",
                            "privateIpAddress": "172.31.36.75",
                            "privateIpAddresses": [
                              {
                                "privateDnsName": "ip-172-31-36-75.us-west-2.compute.internal",
                                "privateIpAddress": "172.31.36.75"
                              }
                            ],
                            "publicDnsName": "ec2-54-202-242-173.us-west-2.compute.amazonaws.com",
                            "publicIp": "54.202.242.173",
                            "securityGroups": [
                              {
                                "groupId": "sg-48578931",
                                "groupName": "default"
                              }
                            ],
                            "subnetId": "subnet-8aeebbfc",
                            "vpcId": "vpc-05515b61"
                          }
                        ],
                        "schemaVersion": 1,
                        "tags": [
                          {
                            "key": "scaling",
                            "value": "yes"
                          },
                          {
                            "key": "aws:autoscaling:groupName",
                            "value": "auto scaling group"
                          },
                          {
                            "key": "Name",
                            "value": "beta_amazon_linux_201803_scaling"
                          },
                          {
                            "key": "beta",
                            "value": "true"
                          }
                        ]
                      },
                     "assetType": "ec2-instance",
                     "attributes": [],
                     "confidence": 10,
                     "createdAt": 1458680301.37,
                     "description": "Amazon Inspector Classic did not find any potential security issues during this assessment.",
                     "indicatorOfCompromise": false,
                     "numericSeverity": 0,
                     "recommendation": "No remediation needed.",
                     "schemaVersion": 1,
                     "service": "Inspector",
                     "serviceAttributes": {
                       "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                       "rulesPackageArn": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP",
                       "schemaVersion": 1
                     },
                     "severity": "Informational",
                     "title": "No potential security issues found",
                     "updatedAt": 1458680301.37,
                     "userAttributes": []
                   }
                 ]
               }
```

## See Also
<a name="API_DescribeFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeFindings)
