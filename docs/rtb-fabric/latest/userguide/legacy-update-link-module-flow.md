---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/userguide/legacy-update-link-module-flow.html
---

# Configuring modules with UpdateLinkModuleFlow (legacy)

**Important**
`UpdateLinkModuleFlow` is a legacy operation and isn't recommended for new links. It supports only built-in modules and can't express phases or `activationPercentage`. To attach built-in or vendor modules, use `PutLinkFlows` or the console. For more information, see [Discovering and attaching modules](discovering-attaching-modules.md).

To add, modify, or remove built-in modules on your links with the API, the AWS Command Line Interface (AWS CLI), or CloudFormation, you can use the [UpdateLinkModuleFlow](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkModuleFlow.html) API operation or its equivalent in the AWS CLI or CloudFormation. CloudFormation doesn't support flows that you set with `PutLinkFlows`, and a stack update to a link's modules replaces them. After you move a link to `PutLinkFlows`, stop using `UpdateLinkModuleFlow` on it.

With `UpdateLinkModuleFlow`, `moduleParameters` selects the module, and modules are applied in the order that you specify. For each module's parameters, see [Built-in module reference](built-in-modules.md).

**Important**
Modules can only be configured on **active** links. Ensure both gateways are in `ACTIVE` status and the link is `ACTIVE` before attempting module configuration.

**Topics**
+ [Rate Limiter Module](#rate-limiter-module-example)
+ [No-bid module](#no-bid-module-example)
+ [OpenRTB Attribute Module](#openrtb-attribute-module-example)
+ [Configuring Multiple Modules](#multiple-modules-example)
+ [Viewing Module Configuration](#viewing-modules)
+ [Removing Modules](#removing-modules)
+ [Troubleshooting](#troubleshooting-modules)

## Rate Limiter Module
<a name="rate-limiter-module-example"></a>

The following example shows how to add a QPS rate limiter module to a link using the AWS Command Line Interface (AWS CLI).

**Add a QPS rate limiter module to a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-source123}} \
--link-id {{link-abc456def}} \
--client-token {{"unique-update-token-789"}} \
--modules {{'[
    {
        "name": "rateLimiterModule",
        "dependsOn": [],
        "moduleParameters": {
            "rateLimiter": {
                "tps": 1000.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

## No-bid module
<a name="no-bid-module-example"></a>

With `UpdateLinkModuleFlow`, the no-bid module takes its share of requests from `passThroughPercentage`, from 0 through 100. That share of requests passes to the next module, and the module returns a no-bid response for the rest. The optional `reason` and `reasonCode` parameters work as described in [No-bid module](built-in-modules.md#no-bid-module). When you move a link to `PutLinkFlows`, set `activationPercentage` to 100 minus `passThroughPercentage`.

The following example returns a no-bid response with reason code 1 for 10 percent of the link's bid requests, and passes the other 90 percent to the next module.

**Add a no-bid module to a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "noBidModule",
        "dependsOn": [],
        "moduleParameters": {
            "noBid": {
                "reasonCode": 1,
                "passThroughPercentage": 90.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

## OpenRTB Attribute Module
<a name="openrtb-attribute-module-example"></a>

With `UpdateLinkModuleFlow`, you specify the OpenRTB Attribute Module configuration inside the `openRtbAttribute` object within `moduleParameters`. It contains `filterConfiguration`, `filterType`, and `action`, as described in [OpenRTB Attribute Module](built-in-modules.md#openrtb-attribute-module), and `holdbackPercentage`.

### Holdback percentage
<a name="openrtb-attribute-module-holdback"></a>

The `holdbackPercentage` field specifies a percentage of requests (from 0.0 to 100.0) that pass through the module without any action being applied, regardless of whether they match the filter configuration. This is useful for A/B testing or for gradually rolling out filtering rules. For example, setting `holdbackPercentage` to `10.0` means 10% of requests bypass the module entirely.

`PutLinkFlows` doesn't accept `holdbackPercentage`. When you move a link to `PutLinkFlows`, set `activationPercentage` to 100 minus `holdbackPercentage` instead.

### Examples
<a name="openrtb-attribute-module-examples"></a>

**Example 1: Block COPPA-flagged traffic from specific countries**

The following example returns an HTTP `204 No Content` for bid requests that have the COPPA flag set to true and originate from the United States or Canada:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            },
                            {
                                "path": "$.device.geo.country",
                                "values": ["USA", "CAN"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {}
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 2: Block traffic from multiple sources using OR logic**

The following example returns a no-bid response for bid requests that match *either* of the following conditions:
+ COPPA flag is true AND the request originates from the United States or Canada
+ The request is from the domain `example.com`

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            },
                            {
                                "path": "$.device.geo.country",
                                "values": ["USA", "CAN"]
                            }
                        ]
                    },
                    {
                        "criteria": [
                            {
                                "path": "$.site.domain",
                                "values": ["example.com"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 3: Tag requests with a custom header**

The following example adds a custom HTTP header to bid requests from mobile devices instead of blocking them. The requests are still forwarded to the DSP with the additional header attached:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.device.devicetype",
                                "values": ["1", "4"]
                            }
                        ]
                    }
                ],
                "action": {
                    "headerTag": {
                        "name": "X-Device-Category",
                        "value": "mobile"
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 4: Block all traffic except from specific domains with holdback**

The following example uses `EXCLUDE` filter type to keep only traffic from `trusted-publisher.com` or `premium-ads.com`, and returns a no-bid response for all other requests. A 5% holdback ensures that a small sample of excluded traffic still passes through for monitoring purposes:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "EXCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.site.domain",
                                "values": ["trusted-publisher.com", "premium-ads.com"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 5.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

## Configuring Multiple Modules
<a name="multiple-modules-example"></a>

The following example shows how to configure multiple modules on a single link using the AWS Command Line Interface (AWS CLI). In this example, the rate limiter module runs first to cap traffic at 1000 TPS, and then the OpenRTB attribute module filters COPPA-flagged requests from the remaining traffic:

**Configure multiple modules on a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "rateLimiterModule",
        "dependsOn": [],
        "moduleParameters": {
            "rateLimiter": {
                "tps": 1000.0
            }
        }
    },
    {
        "name": "openRtbAttributeModule",
        "dependsOn": ["rateLimiterModule"],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

## Viewing Module Configuration
<a name="viewing-modules"></a>

The following example shows how to retrieve the current module configuration for a link using the AWS Command Line Interface (AWS CLI).

**View module configuration for a link**

```
$ aws rtbfabric get-link \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--region {{us-east-1}}
```

The response includes:
+ `flowModules` - Currently active module configuration
+ `pendingFlowModules` - Module configuration pending activation (if any)

## Removing Modules
<a name="removing-modules"></a>

The following example shows how to remove all modules from a link using the AWS Command Line Interface (AWS CLI).

**Remove all modules from a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[]'}} \
--region {{us-east-1}}
```

## Troubleshooting
<a name="troubleshooting-modules"></a>

**Common Issues:**
+ **"Resource not ready to be used yet"** - Wait for gateways and links to reach `ACTIVE` status before configuring modules.
+ **Module configuration not applied** - Check the `pendingFlowModules` field in the link response to see if configuration is still being processed.
+ **Invalid module parameters** - Verify parameter names and value types match the module specification exactly.

The following example shows how to check link and module status using the AWS Command Line Interface (AWS CLI).

**Check link and module status**

```
$ aws rtbfabric get-link \
--gateway-id {{<gateway-id>}} \
--link-id {{<link-id>}} \
--query {{'{Active:flowModules,Pending:pendingFlowModules}'}} \
--region {{us-east-1}}
```
