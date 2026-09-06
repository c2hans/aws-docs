---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-safetyrules.html
---

# ListSafetyRules
<a name="controlpanel-controlpanelarn-safetyrules"></a>

## URI
<a name="controlpanel-controlpanelarn-safetyrules-url"></a>

`/controlpanel/{{ControlPanelArn}}/safetyrules`

## HTTP methods
<a name="controlpanel-controlpanelarn-safetyrules-http-methods"></a>

### GET
<a name="controlpanel-controlpanelarn-safetyrulesget"></a>

**Operation ID:** `ListSafetyRules`

List the safety rules (the assertion rules and gating rules) that you've defined for the routing controls in a control panel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of the control panel. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| MaxResults | String | False | The number of objects that you want to return with this call. |
| NextToken | String | False | The token that identifies which batch of results you want to see. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListSafetyRulesResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="controlpanel-controlpanelarn-safetyrulesoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of a control panel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="controlpanel-controlpanelarn-safetyrules-schemas"></a>

### Response bodies
<a name="controlpanel-controlpanelarn-safetyrules-response-examples"></a>

#### ListSafetyRulesResponse schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-listsafetyrulesresponse-example"></a>

```
{
  "NextToken": "string",
  "SafetyRules": [
    {
      "ASSERTION": {
        "Status": enum,
        "Owner": "string",
        "ControlPanelArn": "string",
        "AssertedControls": [
          "string"
        ],
        "SafetyRuleArn": "string",
        "RuleConfig": {
          "Type": enum,
          "Inverted": boolean,
          "Threshold": integer
        },
        "WaitPeriodMs": integer,
        "Name": "string"
      },
      "GATING": {
        "Status": enum,
        "TargetControls": [
          "string"
        ],
        "Owner": "string",
        "ControlPanelArn": "string",
        "GatingControls": [
          "string"
        ],
        "SafetyRuleArn": "string",
        "RuleConfig": {
          "Type": enum,
          "Inverted": boolean,
          "Threshold": integer
        },
        "WaitPeriodMs": integer,
        "Name": "string"
      }
    }
  ]
}
```

#### ValidationException schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="controlpanel-controlpanelarn-safetyrules-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="controlpanel-controlpanelarn-safetyrules-properties"></a>

### AccessDeniedException
<a name="controlpanel-controlpanelarn-safetyrules-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### AssertionRule
<a name="controlpanel-controlpanelarn-safetyrules-model-assertionrule"></a>

An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met. Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is `On` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertedControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | Name of the assertion rule. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the assertion rule owner. |
| RuleConfig | [RuleConfig](#controlpanel-controlpanelarn-safetyrules-model-ruleconfig) | True | The criteria that you set for specific assertion routing controls (AssertedControls) that designate how many routing control states must be `ON` as the result of a transaction. For example, if you have three assertion routing controls, you might specify `atleast` 2 for your rule configuration. This means that at least two assertion routing control states must be `ON`, so that at least two AWS Regions have traffic flowing to them.  |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the assertion rule. |
| Status | [Status](#controlpanel-controlpanelarn-safetyrules-model-status) | True | The deployment status of an assertion rule. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### GatingRule
<a name="controlpanel-controlpanelarn-safetyrules-model-gatingrule"></a>

A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.

For example, if you specify one gating routing control and you set the `Type` in the rule configuration to `OR`, that indicates that you must set the gating routing control to `On` for the rule to evaluate as true; that is, for the gating control "switch" to be "On". When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| GatingControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | An array of gating routing control Amazon Resource Names (ARNs). For a simple "on/off" switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the gating rule. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the gating rule owner. |
| RuleConfig | [RuleConfig](#controlpanel-controlpanelarn-safetyrules-model-ruleconfig) | True | The criteria that you set for gating routing controls that designate how many of the routing control states must be `ON` to allow you to update target routing control states. |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the gating rule. |
| Status | [Status](#controlpanel-controlpanelarn-safetyrules-model-status) | True | The deployment status of a gating rule. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |
| TargetControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall "on/off" switch for a set of target routing controls. You can use this to manually override automated failover, for example. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### InternalServerException
<a name="controlpanel-controlpanelarn-safetyrules-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListSafetyRulesResponse
<a name="controlpanel-controlpanelarn-safetyrules-model-listsafetyrulesresponse"></a>

The response to a `ListSafetyRulesRequest`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| NextToken | string<br />Pattern: `[\S]*`<br />MinLength: 1<br />MaxLength: 8096 | False | The token that identifies which batch of results you want to see. |
| SafetyRules | Array of type [Rule](#controlpanel-controlpanelarn-safetyrules-model-rule) | False | The list of safety rules in a control panel. |

### ResourceNotFoundException
<a name="controlpanel-controlpanelarn-safetyrules-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Rule
<a name="controlpanel-controlpanelarn-safetyrules-model-rule"></a>

A safety rule. A safety rule can be an assertion rule or a gating rule. To learn more, see <ulink type="documentation" url="r53recovery/latest/dg/routing-control.safety-rules.html">Safety rules</ulink> in the Amazon Application Recovery Controller Developer Guide.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ASSERTION | [AssertionRule](#controlpanel-controlpanelarn-safetyrules-model-assertionrule) | False | An assertion rule enforces that, when a routing control state is changed, the criteria set by the rule configuration is met. Otherwise, the change to the routing control state is not accepted. For example, the criteria might be that at least one routing control state is `On` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario. |
| GATING | [GatingRule](#controlpanel-controlpanelarn-safetyrules-model-gatingrule) | False | A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.<br />For example, if you specify one gating routing control and you set the `Type` in the rule configuration to `OR`, that indicates that you must set the gating routing control to `On` for the rule to evaluate as true; that is, for the gating control "switch" to be "On". When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule. |

### RuleConfig
<a name="controlpanel-controlpanelarn-safetyrules-model-ruleconfig"></a>

The rule configuration for an assertion rule. That is, the criteria that you set for specific assertion controls (routing controls) that specify how many control states must be `ON` after a transaction completes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Inverted | boolean | True | Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa. |
| Threshold | integer<br />Format: int32 | True | The value of N, when you specify an `ATLEAST` rule type. That is, `Threshold` is the number of controls that must be set when you specify an `ATLEAST` type. |
| Type | [RuleType](#controlpanel-controlpanelarn-safetyrules-model-ruletype) | True | A rule can be one of the following: `ATLEAST`, `AND`, or `OR`. |

### RuleType
<a name="controlpanel-controlpanelarn-safetyrules-model-ruletype"></a>

An enumerated type that determines how the evaluated rules are processed. `RuleType` can be one of the following:

ATLEAST - At least N routing controls must be set. You specify N as the `Threshold` in the rule configuration.

AND - All routing controls must be set. This is a shortcut for "At least N," where N is the total number of controls in the rule.

OR - Any control must be set. This is a shortcut for "At least N," where N is 1.
+ `ATLEAST`
+ `AND`
+ `OR`

### Status
<a name="controlpanel-controlpanelarn-safetyrules-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="controlpanel-controlpanelarn-safetyrules-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="controlpanel-controlpanelarn-safetyrules-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="controlpanel-controlpanelarn-safetyrules-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListSafetyRules
<a name="ListSafetyRules-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/ListSafetyRules)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListSafetyRules)
