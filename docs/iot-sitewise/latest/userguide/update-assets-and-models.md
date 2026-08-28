---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html
---

# Update assets and models
<a name="update-assets-and-models"></a>

You can update your assets, asset models, component models, and interfaces in AWS IoT SiteWise to modify their names and definitions. These update operations are asynchronous and take time to propagate through AWS IoT SiteWise. Check the status of the asset or model before you make additional changes. You must wait until the changes propagate before you can continue to use the updated asset or model.

**Topics**
+ [Update assets in AWS IoT SiteWise](update-assets.md)
+ [Update asset models, component models, and interfaces](update-asset-models.md)
+ [Update custom composite models (components)](update-custom-composite-models.md)
+ [Optimistic locking for asset model writes](opt-locking-for-model.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
