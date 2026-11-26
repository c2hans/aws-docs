---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/userguide/built-in-modules.html
---

# Built-in module reference

RTB Fabric provides the following built-in modules that you can configure for your links. Built-in modules are available at no additional charge and don't need a subscription. To attach them, use `PutLinkFlows` or the console, as described in [Discovering and attaching modules](discovering-attaching-modules.md). With `PutLinkFlows`, you pass a module's parameters as a JSON string in `configurationValues`. Built-in modules also have rules for their flow settings. For more information, see [Rules for built-in modules](discovering-attaching-modules.md#built-in-module-rules).

**Topics**
+ [Rate Limiter Module](#rate-limiter-module)
+ [No-bid module](#no-bid-module)
+ [OpenRTB Attribute Module](#openrtb-attribute-module)

## Rate Limiter Module
<a name="rate-limiter-module"></a>

The Rate Limiter Module controls the rate of requests flowing through the link by limiting transactions per second (TPS). This module helps protect downstream systems from traffic spikes and ensures consistent performance under varying load conditions.

The Rate Limiter Module has the following module ID, version, and parameter:
+ Module ID and version – `module-rateLimiter`, 1.0.0.
+ `tps` (required) – The maximum transactions per second, from 1 through 16,777,216.

## No-bid module
<a name="no-bid-module"></a>

The no-bid module returns a no-bid response for a share of bid requests on the link without forwarding them. The no-bid module is available with `PutLinkFlows` and `UpdateLinkModuleFlow`, which set that share in different ways:
+ With `PutLinkFlows`, `activationPercentage` is required and sets the share of requests that the module answers.
+ With `UpdateLinkModuleFlow`, `passThroughPercentage` sets the share of requests that the module passes to the next module without answering them. The module answers the rest. For an example, see [No-bid module](legacy-update-link-module-flow.md#no-bid-module-example).

The no-bid module has the following module ID, version, and parameters:
+ Module ID and version – `module-noBid`, 1.0.0.
+ `reason` (optional) – Up to 50 letters and digits. `reason` labels the module's log events and isn't returned in the response.
+ `reasonCode` (optional) – 0 through 10. With `reasonCode`, the response is HTTP 200 with the code as `nbr`. Without it, the response is HTTP 204 with no body.

## OpenRTB Attribute Module
<a name="openrtb-attribute-module"></a>

The OpenRTB Attribute Module filters bid requests based on attributes in the OpenRTB request payload. You define a set of filters to divide incoming bid requests into two groups: requests that match your filters and requests that do not. You then choose which group to apply an action to, such as returning a no-bid response or adding a custom HTTP header. This lets you intelligently shed traffic before it reaches your DSP, reducing compute and networking costs.

**Warning**
A misconfigured OpenRTB Attribute Module can unintentionally block desirable traffic. If you are unsure of the impact of a new filter configuration, start the module on a small share of requests, and increase the share gradually as you verify that only the intended traffic is being filtered. With `PutLinkFlows`, set a low `activationPercentage` (for example, 10). With `UpdateLinkModuleFlow`, set a high `holdbackPercentage` (for example, 90.0).

Module ID and version: `module-openrtbAttributeFilter`, 2.0.0

The module configuration contains the following fields:
+ `filterConfiguration` – An array of filters that define which bid requests to match.
+ `filterType` – Determines which group of requests the action applies to.
+ `action` (optional with `PutLinkFlows`) – The action to perform on the selected group of requests. If you omit it, the module returns a no-bid response with no reason code, which is an HTTP `204 No Content` response.

With `PutLinkFlows`, the module exposes two configurable actions. You don't need to set `selectedActions` for this module. If you set it, select exactly one action, and match it to the module's `action`:
+ `FILTER` – For a `noBid` action, or when you omit `action`.
+ `ENRICH_REQUEST_HEADERS` – For a `headerTag` action.

A request that selects both actions, or an action that the module doesn't expose, fails with a validation error.

With `PutLinkFlows`, you pass these fields in `configurationValues`. With `UpdateLinkModuleFlow`, you put them in the `openRtbAttribute` object within `moduleParameters`, which also accepts `holdbackPercentage`. For more information, see [Holdback percentage](legacy-update-link-module-flow.md#openrtb-attribute-module-holdback).

### Filter criteria
<a name="openrtb-attribute-module-filter-criteria"></a>

A *filter criterion* is the smallest unit of a filter. Each criterion is a predicate on a single field in the OpenRTB bid request. A criterion contains two fields:
+ `path` – A JSONPath expression that identifies a single field in the bid request body (for example, `$.device.geo.country`). For the supported syntax, see the rules that follow this list.
+ `values` – An array of strings representing the desired values. A criterion matches when the value retrieved from the bid request field is contained in this array.

A `path` must select exactly one field. It starts with `$`, followed by one or more of these segments:
+ `.{{name}}` – For example, `$.device.geo.country`.
+ `['{{name}}']` or `["{{name}}"]` – For a name that contains characters such as hyphens. For example, `$.ext['some-key']`.
+ `[{{index}}]` – For an array element. For example, `$.imp[0].tagid`.

Wildcards (such as `$.imp[*].tagid`), filter expressions, slices, and whitespace outside quoted names aren't supported. `PutLinkFlows` rejects a path that doesn't follow these rules with a validation error.

The following example criterion matches bid requests where the COPPA (Children's Online Privacy Protection Act) flag is set to `1` (true):

```
{
    "path": "$.regs.coppa",
    "values": ["1"]
}
```

The following example criterion matches bid requests originating from the United States or Canada:

```
{
    "path": "$.device.geo.country",
    "values": ["USA", "CAN"]
}
```

**Note**
The `values` field uses string matching. Numeric fields in the OpenRTB specification (such as `regs.coppa`) must be represented as strings in the `values` array (for example, `"1"` instead of `1`).

### Filters
<a name="openrtb-attribute-module-filters"></a>

A *filter* groups one or more filter criteria together using **AND** logic. All criteria within a filter must match for the filter to match a bid request. A filter contains a single field:
+ `criteria` – An array of filter criterion objects.

The following example filter matches bid requests that have the COPPA flag set to true **AND** originate from the United States or Canada. Both criteria must be satisfied:

```
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
```

### Filter configuration
<a name="openrtb-attribute-module-filter-configuration"></a>

The `filterConfiguration` field is an array of filters combined using **OR** logic. A bid request matches the filter configuration if it matches *any one* of the filters in the array.

By combining AND logic within each filter and OR logic across filters, you can express complex filtering rules. The following example matches two types of requests:
+ Type A: Requests with COPPA flag set to true **AND** originating from the United States or Canada
+ **OR**
+ Type B: Requests from the domain `example.com`

```
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
]
```

### Filter type
<a name="openrtb-attribute-module-filter-type"></a>

The `filterType` field determines which group of bid requests the action applies to. After the filter configuration divides requests into two groups (matched and unmatched), the filter type selects which group receives the action.
+ `INCLUDE` – The action is performed on requests that *match* the filter configuration. Use this when you want to target specific types of traffic (for example, block requests from certain regions).
+ `EXCLUDE` – The action is performed on requests that *do not match* the filter configuration. Use this when you want to define the traffic you want to keep and apply the action to everything else.

### Actions
<a name="openrtb-attribute-module-actions"></a>

The `action` field specifies what to do with the selected group of bid requests. The following actions are available:
+ **No bid** (`noBid`) – Short-circuits the request and returns a no-bid response without forwarding it to the DSP.

  If you omit the `noBidReasonCode` field, the module returns an HTTP `204 No Content` response with no response body:

  ```
  "action": {
      "noBid": {}
  }
  ```

  If you specify a `noBidReasonCode`, the module returns an HTTP `200 OK` response with a JSON body containing the request ID (if present in the original bid request) and an `nbr` field set to the reason code you provided:

  ```
  "action": {
      "noBid": {
          "noBidReasonCode": 1
      }
  }

  // Example response body:
  // { "id": "request-123", "nbr": 1 }
  ```
+ **Header tag** (`headerTag`) – Adds a custom HTTP header to the request before forwarding it to the DSP. The request is not blocked; instead it is tagged with additional metadata. You specify a header `name` and `value`.

  You can't use a header that frames the request or that RTB Fabric sets itself. `PutLinkFlows` rejects the following names with a validation error, regardless of case:
  + `Connection`, `Keep-Alive`, `Proxy-Connection`, `TE`, `Trailer`, `Transfer-Encoding`, and `Upgrade`
  + `Content-Length`, `Content-Encoding`, and `Host`
  + `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Port`, and `X-Forwarded-Proto`
  + Any name that starts with `x-amz-` or `x-amzn-`

  RTB Fabric might also reserve other names for headers that it sets itself.

  ```
  "action": {
      "headerTag": {
          "name": "X-Custom-Filter",
          "value": "coppa-flagged"
      }
  }
  ```
