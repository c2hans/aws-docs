---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/processing-plugin.html
---

# Processing plugin
<a name="processing-plugin"></a>

 There are two types of plugins: **transformer** and **enrichment**. You can choose to have only one **transformer**, and zero or multiple **enrichment**.

## Built-in plugins
<a name="built-in-plugins"></a>

 Below plugins are provided by Clickstream Analytics on AWS.

|  **Plugin name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  UAEnrichment  |  enrichment  |  User-agent enrichment, use ua\_parser Java library to enrich User-Agent in the HTTP header to ua\_browser,ua\_browser\_version,ua\_os,ua\_os\_version,ua\_device  |
|  IpEnrichment  |  enrichment  |  IP address enrichment, use GeoLite2 data by MaxMind to enrich IP to city, continent, country  |

 The UAEnrichment uses [UA Parser](https://mvnrepository.com/artifact/ua_parser/ua-parser) to parse user-agent in Http header

 The IpEnrichment plugin uses [GeoLite2-City data](https://cdn.jsdelivr.net/npm/geolite2-city@1.0.0/GeoLite2-City.mmdb.gz) created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/)

## Custom plugins
<a name="custom-plugins"></a>

 You can add custom plugins to transform raw event data or enrich the data for your need.

**Note**
 To add custom plugins, you must develop your own plugins firstly, see [Develop Custom Plugins](#develop-custom-plugins).

 To add your plugins, choose **Add Plugin**, which will open a new window, in which you can upload your plugins.

1.  Enter the plugin **Name** and **Description**

1.  Choose **Plugin Type**

1.  **Enrichment**: Plugin to add fields into event data collected by SDK (both Clickstream SDK or third-party SDK)

1.  **Transformation**: A plugin used to transform a third-party SDK’s raw data into guidance built-in schema

1.  Upload plugin java JAR file

1.  (Optional) Upload the dependency files if any

1.  **Main function class**: fill the full class name of your plugin class name, e.g. com.company.sol.CustomTransformer

## Develop Custom Plugins
<a name="develop-custom-plugins"></a>

 The simplest way to develop custom plugins is making changes based on our example project.

1.  Clone/Fork the example project.

   ```
   git clone https://github.com/aws-solutions-library-samples/guidance-for-clickstream-analytics-on-aws.git
   cd examples/custom-plugins
   ```
   +  For enrichment plugin, please refer to the example: `custom-enrich/ `
   +  For transformer plugin, please refer to the example: `custom-sdk-transformer/ `

1.  Change packages and classes name as you desired.

1.  Implement the method `public Dataset<row> transform(Dataset<row> dataset)` to do transformation or enrichment.

1.  (Optional) Write test code.

1.  Run gradle to package code to jar `./gradlew clean build`.

1.  Get the jar file in build output directory `./build/libs/`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
