---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-region.html
---

# Region changes
<a name="migration-client-region"></a>

This section describes the changes implemented in the AWS SDK for Java 2.x for using the `Region` and `Regions` classes.

## Region configuration
<a name="region-configuration"></a>
+ Some AWS services don’t have Region specific endpoints. When using those services, you must set the Region as `Region.AWS_GLOBAL` or `Region.AWS_CN_GLOBAL`.
**Example**

  ```
  Region region = Region.AWS_GLOBAL;
  ```
+  `com.amazonaws.regions.Regions` and `com.amazonaws.regions.Region` classes are now combined into one class, `software.amazon.awssdk.regions.Region`.

## Method and class name mappings
<a name="region-method-mapping"></a>

The following tables map Region related classes between versions 1.x and 2.x of the AWS SDK for Java. You can create an instance of these classes using the `of()` method.

**Example**

```
RegionMetadata regionMetadata = RegionMetadata.of(Region.US_EAST_1);
```

**1.x Regions class method changes**

| 1.x | 2.x |
| --- | --- |
| `Regions.fromName` | `Region.of` |
| `Regions.getName` | `Region.id` |
| `Regions.getDescription` | `Region.metadata().description()` |
| `Regions.getCurrentRegion` | Not Supported |
| `Regions.DEFAULT_REGION` | Not Supported |
| `Regions.name` | `Region.id` |

**1.x Region class method changes**

| 1.x | 2.x |
| --- | --- |
| `Region.getName` | `Region.id` |
| `Region.hasHttpsEndpoint` | Not Supported |
| `Region.hasHttpEndpoint` | Not Supported |
| `Region.getAvailableEndpoints` | Not Supported |
| `Region.createClient` | Not Supported |

**RegionMetadata class method changes**

| 1.x | 2.x |
| --- | --- |
| `RegionMetadata.getName` | `RegionMetadata.name` |
| `RegionMetadata.getDomain` | `RegionMetadata.domain` |
| `RegionMetadata.getPartition` | `RegionMetadata.partition` |

**ServiceMetadata class method changes**

| 1.x | 2.x |
| --- | --- |
| `Region.getServiceEndpoint` | `ServiceMetadata.endpointFor(Region)` |
| `Region.isServiceSupported` | `ServiceMetadata.regions().contains(Region)` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
