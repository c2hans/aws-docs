---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint
<a name="aws-resource-lambda-webfunctionendpoint"></a>

The `AWS::Lambda::WebFunctionEndpoint` resource creates an endpoint for a Lambda web function. An endpoint exposes the web function over HTTPS and routes traffic to one or more revisions. The endpoint type determines how the endpoint serves and routes traffic across Regions. For canary or blue-green deployments, you can split traffic between two revisions. To do this, specify two entries in the `RevisionWeights` property.

## Syntax
<a name="aws-resource-lambda-webfunctionendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunctionendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunctionEndpoint",
  "Properties" : {
      "[AuthType](#cfn-lambda-webfunctionendpoint-authtype)" : {{String}},
      "[Description](#cfn-lambda-webfunctionendpoint-description)" : {{String}},
      "[EndpointName](#cfn-lambda-webfunctionendpoint-endpointname)" : {{String}},
      "[EndpointType](#cfn-lambda-webfunctionendpoint-endpointtype)" : {{String}},
      "[FunctionName](#cfn-lambda-webfunctionendpoint-functionname)" : {{String}},
      "[Regions](#cfn-lambda-webfunctionendpoint-regions)" : {{[ String, ... ]}},
      "[RevisionWeights](#cfn-lambda-webfunctionendpoint-revisionweights)" : {{[ RevisionWeight, ... ]}},
      "[ScalingConfig](#cfn-lambda-webfunctionendpoint-scalingconfig)" : {{ScalingConfig}},
      "[ThrottleConfig](#cfn-lambda-webfunctionendpoint-throttleconfig)" : {{ThrottleConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunctionendpoint-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunctionEndpoint
Properties:
  [AuthType](#cfn-lambda-webfunctionendpoint-authtype): {{String}}
  [Description](#cfn-lambda-webfunctionendpoint-description): {{String}}
  [EndpointName](#cfn-lambda-webfunctionendpoint-endpointname): {{String}}
  [EndpointType](#cfn-lambda-webfunctionendpoint-endpointtype): {{String}}
  [FunctionName](#cfn-lambda-webfunctionendpoint-functionname): {{String}}
  [Regions](#cfn-lambda-webfunctionendpoint-regions): {{
    - String}}
  [RevisionWeights](#cfn-lambda-webfunctionendpoint-revisionweights): {{
    - RevisionWeight}}
  [ScalingConfig](#cfn-lambda-webfunctionendpoint-scalingconfig): {{
    ScalingConfig}}
  [ThrottleConfig](#cfn-lambda-webfunctionendpoint-throttleconfig): {{
    ThrottleConfig}}
```

## Properties
<a name="aws-resource-lambda-webfunctionendpoint-properties"></a>

`AuthType`  <a name="cfn-lambda-webfunctionendpoint-authtype"></a>
The authorization type for the endpoint.
Valid values:
+ `ApplicationManaged` – Your application handles authorization.
+ `IamAuth` – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).
*Required*: Yes
*Type*: String
*Allowed values*: `ApplicationManaged | IamAuth`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lambda-webfunctionendpoint-description"></a>
A description of the endpoint.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-lambda-webfunctionendpoint-endpointname"></a>
The name of the endpoint to create. The name can contain letters, numbers, hyphens (-), and underscores (\_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointType`  <a name="cfn-lambda-webfunctionendpoint-endpointtype"></a>
The type of endpoint to create. Determines how traffic is served and routed across Regions.
Valid values:
+ `HomeRegion` – Serves traffic from the Region where you created the web function.
+ `MultiRegion` – Replicates across the Regions that you choose and routes each request to the nearest one.
+ `PerRegion` – Creates a separate endpoint in each Region that you choose.
*Required*: Yes
*Type*: String
*Allowed values*: `HomeRegion | MultiRegion | PerRegion`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-lambda-webfunctionendpoint-functionname"></a>
The web function to create the endpoint for.
You can specify either of the following:
+ The function name, for example `my-function`.
+ The function ARN, for example `arn:aws:lambda:us-east-1:111122223333:web-function/my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regions`  <a name="cfn-lambda-webfunctionendpoint-regions"></a>
The list of Regions the endpoint is deployed to. Required when the endpoint type is `MultiRegion` or `PerRegion`: specify at least one Region other than the Region where you create the endpoint (the home Region). The home Region is added automatically if you don't include it. You can't specify only the home Region. When the endpoint type is `HomeRegion`, omit this property or specify only the home Region.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RevisionWeights`  <a name="cfn-lambda-webfunctionendpoint-revisionweights"></a>
A list of revision weights that determine how traffic is distributed across revisions. You can specify up to two revisions for canary or blue-green deployments.
*Required*: No
*Type*: Array of [RevisionWeight](aws-properties-lambda-webfunctionendpoint-revisionweight.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfig`  <a name="cfn-lambda-webfunctionendpoint-scalingconfig"></a>
The scaling configuration for the endpoint. Optionally constrains how many concurrent execution environments the endpoint can use, in addition to your account's vCPU quota.
*Required*: No
*Type*: [ScalingConfig](aws-properties-lambda-webfunctionendpoint-scalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottleConfig`  <a name="cfn-lambda-webfunctionendpoint-throttleconfig"></a>
The throttling configuration for the endpoint. Optionally constrains the request rate that the endpoint accepts, in addition to your account's rate limit quota.
*Required*: No
*Type*: [ThrottleConfig](aws-properties-lambda-webfunctionendpoint-throttleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-webfunctionendpoint-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunctionendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the endpoint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-webfunctionendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

 `RegionalEndpoints`
A map of the endpoint's per-Region configuration and state. Each key is a Region code, for example `us-east-1`. Each value is a [RegionalEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-regionalendpoint.html) object.

####
<a name="aws-resource-lambda-webfunctionendpoint-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the endpoint was created.

`DomainName`  <a name="DomainName-fn::getatt"></a>
The domain name assigned to the endpoint.

`EndpointArn`  <a name="EndpointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the endpoint.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the web function.

`State`  <a name="State-fn::getatt"></a>
The current state of the endpoint.

`StateReason`  <a name="StateReason-fn::getatt"></a>
The reason for the current state of the endpoint.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the endpoint was last updated.

`UpdateStatus`  <a name="UpdateStatus-fn::getatt"></a>
The status of the most recent update to the endpoint.

`UpdateStatusReason`  <a name="UpdateStatusReason-fn::getatt"></a>
The reason for the endpoint's most recent update status.

## Examples
<a name="aws-resource-lambda-webfunctionendpoint--examples"></a>

### Web function endpoint
<a name="aws-resource-lambda-webfunctionendpoint--examples--Web_function_endpoint"></a>

Create an endpoint that routes all traffic to one revision of the web function `my-web-function`.

#### JSON
<a name="aws-resource-lambda-webfunctionendpoint--examples--Web_function_endpoint--json"></a>

```
"MyEndpoint": {
    "Type": "AWS::Lambda::WebFunctionEndpoint",
    "Properties": {
        "FunctionName": "my-web-function",
        "EndpointName": "my-endpoint",
        "EndpointType": "HomeRegion",
        "AuthType": "IamAuth",
        "RevisionWeights": [
            {
                "RevisionId": {
                    "Fn::GetAtt": [
                        "MyRevision",
                        "RevisionId"
                    ]
                },
                "Weight": 100
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-lambda-webfunctionendpoint--examples--Web_function_endpoint--yaml"></a>

```
MyEndpoint:
  Type: AWS::Lambda::WebFunctionEndpoint
  Properties:
    FunctionName: my-web-function
    EndpointName: my-endpoint
    EndpointType: HomeRegion
    AuthType: IamAuth
    RevisionWeights:
      - RevisionId: !GetAtt MyRevision.RevisionId
        Weight: 100
```
