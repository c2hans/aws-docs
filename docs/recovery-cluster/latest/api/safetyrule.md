---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html
---

# CreateSafetyRule, UpdateSafetyRule
<a name="safetyrule"></a>

## URI
<a name="safetyrule-url"></a>

`/safetyrule`

## HTTP methods
<a name="safetyrule-http-methods"></a>

### POST
<a name="safetyrulepost"></a>

**Operation ID:** `CreateSafetyRule`

Creates a safety rule in a control panel. Safety rules let you add safeguards around changing routing control states, and for enabling and disabling routing controls, to help prevent unexpected outcomes.

There are two types of safety rules: assertion rules and gating rules.

Assertion rule: An assertion rule enforces that, when you change a routing control state, that a certain criteria is met. For example, the criteria might be that at least one routing control state is `On` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.

Gating rule: A gating rule lets you configure a gating routing control as an overall "on/off" switch for a group of routing controls. Or, you can configure more complex gating scenarios, for example by configuring multiple gating routing controls.

Note that the name of a safety rule must be unique within a control panel.

For more information, see [Safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html) in the Amazon Application Recovery Controller Developer Guide.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateSafetyRuleResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### PUT
<a name="safetyruleput"></a>

**Operation ID:** `UpdateSafetyRule`

Update a safety rule (an assertion rule or gating rule). You can only update the name and the waiting period for a safety rule. To make other updates, delete the safety rule and create a new one.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateSafetyRuleResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="safetyruleoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="safetyrule-schemas"></a>

### Request bodies
<a name="safetyrule-request-examples"></a>

#### POST schema
<a name="safetyrule-request-body-post-example"></a>

```
{
  "AssertionRule": {
    "ControlPanelArn": "string",
    "AssertedControls": [
      "string"
    ],
    "RuleConfig": {
      "Type": enum,
      "Inverted": boolean,
      "Threshold": integer
    },
    "WaitPeriodMs": integer,
    "Name": "string"
  },
  "ClientToken": "string",
  "GatingRule": {
    "TargetControls": [
      "string"
    ],
    "ControlPanelArn": "string",
    "GatingControls": [
      "string"
    ],
    "RuleConfig": {
      "Type": enum,
      "Inverted": boolean,
      "Threshold": integer
    },
    "WaitPeriodMs": integer,
    "Name": "string"
  },
  "Tags": {
  }
}
```

#### PUT schema
<a name="safetyrule-request-body-put-example"></a>

```
{
  "GatingRuleUpdate": {
    "SafetyRuleArn": "string",
    "WaitPeriodMs": integer,
    "Name": "string"
  },
  "AssertionRuleUpdate": {
    "SafetyRuleArn": "string",
    "WaitPeriodMs": integer,
    "Name": "string"
  }
}
```

### Response bodies
<a name="safetyrule-response-examples"></a>

#### CreateSafetyRuleResponse schema
<a name="safetyrule-response-body-createsafetyruleresponse-example"></a>

```
{
  "AssertionRule": {
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
  "GatingRule": {
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
```

#### UpdateSafetyRuleResponse schema
<a name="safetyrule-response-body-updatesafetyruleresponse-example"></a>

```
{
  "AssertionRule": {
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
  "GatingRule": {
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
```

#### ValidationException schema
<a name="safetyrule-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="safetyrule-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="safetyrule-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="safetyrule-properties"></a>

### AssertionRule
<a name="safetyrule-model-assertionrule"></a>

An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met. Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is `On` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertedControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | Name of the assertion rule. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the assertion rule owner. |
| RuleConfig | [RuleConfig](#safetyrule-model-ruleconfig) | True | The criteria that you set for specific assertion routing controls (AssertedControls) that designate how many routing control states must be `ON` as the result of a transaction. For example, if you have three assertion routing controls, you might specify `atleast` 2 for your rule configuration. This means that at least two assertion routing control states must be `ON`, so that at least two AWS Regions have traffic flowing to them.  |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the assertion rule. |
| Status | [Status](#safetyrule-model-status) | True | The deployment status of an assertion rule. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### AssertionRuleUpdate
<a name="safetyrule-model-assertionruleupdate"></a>

An update to an assertion rule. You can update the name or the evaluation period (wait period). If you don't specify one of the items to update, the item is unchanged.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the assertion rule. The name must be unique within a control panel. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the assertion rule. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### CreateSafetyRuleRequest
<a name="safetyrule-model-createsafetyrulerequest"></a>

Request to create a safety rule. You can create either an assertion rule or a gating rule with a `CreateSafetyRuleRequest` call. To learn more, [Safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html) in the Amazon Application Recovery Controller Developer Guide.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertionRule | [NewAssertionRule](#safetyrule-model-newassertionrule) | False | The assertion rule requested. |
| ClientToken | string<br />Pattern: `^[-a-z-A-z0-9 ]+$`<br />MinLength: 1<br />MaxLength: 64 | False | A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request. |
| GatingRule | [NewGatingRule](#safetyrule-model-newgatingrule) | False | The gating rule requested. |
| Tags | object | False | The tags associated with the safety rule. |

### CreateSafetyRuleResponse
<a name="safetyrule-model-createsafetyruleresponse"></a>

The result of a successful `CreateSafetyRule` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertionRule | [AssertionRule](#safetyrule-model-assertionrule) | False | The assertion rule created. |
| GatingRule | [GatingRule](#safetyrule-model-gatingrule) | False | The gating rule created. |

### GatingRule
<a name="safetyrule-model-gatingrule"></a>

A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.

For example, if you specify one gating routing control and you set the `Type` in the rule configuration to `OR`, that indicates that you must set the gating routing control to `On` for the rule to evaluate as true; that is, for the gating control "switch" to be "On". When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| GatingControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | An array of gating routing control Amazon Resource Names (ARNs). For a simple "on/off" switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the gating rule. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the gating rule owner. |
| RuleConfig | [RuleConfig](#safetyrule-model-ruleconfig) | True | The criteria that you set for gating routing controls that designate how many of the routing control states must be `ON` to allow you to update target routing control states. |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the gating rule. |
| Status | [Status](#safetyrule-model-status) | True | The deployment status of a gating rule. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |
| TargetControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall "on/off" switch for a set of target routing controls. You can use this to manually override automated failover, for example. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### GatingRuleUpdate
<a name="safetyrule-model-gatingruleupdate"></a>

Update to a gating rule. You can update the name or the evaluation period (wait period). If you don't specify one of the items to update, the item is unchanged.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the gating rule. The name must be unique within a control panel. Note that only ASCII characters are supported for gating rule names. |
| SafetyRuleArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the gating rule. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### InternalServerException
<a name="safetyrule-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### NewAssertionRule
<a name="safetyrule-model-newassertionrule"></a>

A new assertion rule for a control panel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertedControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the control panel. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the assertion rule. The name must be unique within a control panel. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |
| RuleConfig | [RuleConfig](#safetyrule-model-ruleconfig) | True | The criteria that you set for specific assertion controls (routing controls) that designate how many control states must be `ON` as the result of a transaction. For example, if you have three assertion controls, you might specify `ATLEAST 2` for your rule configuration. This means that at least two assertion controls must be `ON`, so that at least two AWS Regions have traffic flowing to them.  |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### NewGatingRule
<a name="safetyrule-model-newgatingrule"></a>

A new gating rule for a control panel. To learn more, [Safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html) in the Amazon Application Recovery Controller Developer Guide.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| GatingControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The gating controls for the new gating rule. That is, routing controls that are evaluated by the rule configuration that you specify. To learn more, [Safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html) in the Amazon Application Recovery Controller Developer Guide. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name for the new gating rule. |
| RuleConfig | [RuleConfig](#safetyrule-model-ruleconfig) | True | The criteria that you set for specific gating controls (routing controls) that designate how many control states must be `ON` to allow you to change (set or unset) the target control states.  |
| TargetControls | Array of type string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | Routing controls that can only be set or unset if the specified `RuleConfig` evaluates to true for the specified `GatingControls`. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify `ATLEAST 2` as your `RuleConfig`. With these settings, you can only change (set or unset) the routing controls that you have specified as `TargetControls` if that rule evaluates to true. <br />In other words, your ability to change the routing controls that you have specified as `TargetControls` is gated by the rule that you set for the routing controls in `GatingControls`. |
| WaitPeriodMs | integer<br />Format: int32 | True | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value. |

### ResourceNotFoundException
<a name="safetyrule-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### RuleConfig
<a name="safetyrule-model-ruleconfig"></a>

The rule configuration for an assertion rule. That is, the criteria that you set for specific assertion controls (routing controls) that specify how many control states must be `ON` after a transaction completes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Inverted | boolean | True | Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa. |
| Threshold | integer<br />Format: int32 | True | The value of N, when you specify an `ATLEAST` rule type. That is, `Threshold` is the number of controls that must be set when you specify an `ATLEAST` type. |
| Type | [RuleType](#safetyrule-model-ruletype) | True | A rule can be one of the following: `ATLEAST`, `AND`, or `OR`. |

### RuleType
<a name="safetyrule-model-ruletype"></a>

An enumerated type that determines how the evaluated rules are processed. `RuleType` can be one of the following:

ATLEAST - At least N routing controls must be set. You specify N as the `Threshold` in the rule configuration.

AND - All routing controls must be set. This is a shortcut for "At least N," where N is the total number of controls in the rule.

OR - Any control must be set. This is a shortcut for "At least N," where N is 1.
+ `ATLEAST`
+ `AND`
+ `OR`

### Status
<a name="safetyrule-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### UpdateSafetyRuleRequest
<a name="safetyrule-model-updatesafetyrulerequest"></a>

Request to update a safety rule. A safety rule can be an assertion rule or a gating rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertionRuleUpdate | [AssertionRuleUpdate](#safetyrule-model-assertionruleupdate) | False | The assertion rule to update. |
| GatingRuleUpdate | [GatingRuleUpdate](#safetyrule-model-gatingruleupdate) | False | The gating rule to update. |

### UpdateSafetyRuleResponse
<a name="safetyrule-model-updatesafetyruleresponse"></a>

The result of a successful `UpdateSafetyRule` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AssertionRule | [AssertionRule](#safetyrule-model-assertionrule) | False | The assertion rule updated. |
| GatingRule | [GatingRule](#safetyrule-model-gatingrule) | False | The gating rule updated. |

### ValidationException
<a name="safetyrule-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="safetyrule-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateSafetyRule
<a name="CreateSafetyRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/route53-recovery-control-config-2020-11-02/CreateSafetyRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/CreateSafetyRule)

### UpdateSafetyRule
<a name="UpdateSafetyRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)
