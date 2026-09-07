---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/configuring.html
---

# Configuring AWS SDK for SAP ABAP
<a name="configuring"></a>

Before using AWS SDK for SAP ABAP, you must configure the SDK with technical and functional settings that are necessary for the SDK operations. Some settings are transportable and some are runtime settings. Many of the settings are directly analogous to the settings defined in `.INI` files for other SDKs.

The SDK configurations, except for Runtime settings, must be completed in your development environment. You can transport configurations to QA and production following the usual transport and change control rules. Transportable configuration is not recommended for production environments.

If you do not have permissions to configure AWS SDK, see [SAP authorizations](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html).

**Configuring AWS SDK for SAP ABAP**

To run the configuration transaction, enter `/n/AWS1/IMG` in the SAPGUI command bar.

**Configuring AWS SDK for SAP ABAP - BTP edition**

Use the following steps to configure SDK for SAP ABAP - BTP edition.

1. Open your ABAP environment in a web browser.

1. Navigate to Custom Business Configurations application.

To create a customizing request using the Export Customizing Transports application, see [Working in the Export Customizing Transports App - Create Request](https://help.sap.com/docs/btp/sap-business-technology-platform/working-in-export-customizing-transports-app#create-request).

In the Custom Business Configuration application, you can group configurations based on the type of SDK settings. Use the following steps to group configurations.

1. Open your ABAP environment in a web browser, and navigate to the Custom Business Configurations application.

1. Select **Settings** > **Group**, and choose **Configuration Group** from the drop-down list. Select **OK**.

1. The configurations are now available in a hierarchical structure as displayed in the image. To save the view, see [Views (Variant Management) - Components](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/).
![An example of grouped configurations.](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/custom-business-configurations.png)

This section covers the following topics.

**Topics**
+ [Global settings](global-settings.md)
+ [Application configuration](application-configuration.md)
+ [Runtime settings](runtime-settings.md)
+ [Advanced connectivity scenarios](connectivity-scenarios.md)
+ [Service provider settings](service-provider-settings.md)
+ [Refresh, trace, and telemetry topics for AWS SDK for SAP ABAP](additional-setup.md)
