---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialdatasourceitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialDataSourceItem
<a name="aws-properties-quicksight-dashboard-geospatialdatasourceitem"></a>

The data source properties for the geospatial data.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialdatasourceitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialdatasourceitem-syntax.json"></a>

```
{
  "[StaticFileDataSource](#cfn-quicksight-dashboard-geospatialdatasourceitem-staticfiledatasource)" : {{GeospatialStaticFileSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialdatasourceitem-syntax.yaml"></a>

```
  [StaticFileDataSource](#cfn-quicksight-dashboard-geospatialdatasourceitem-staticfiledatasource): {{
    GeospatialStaticFileSource}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialdatasourceitem-properties"></a>

`StaticFileDataSource`  <a name="cfn-quicksight-dashboard-geospatialdatasourceitem-staticfiledatasource"></a>
The static file data source properties for the geospatial data.
*Required*: No
*Type*: [GeospatialStaticFileSource](aws-properties-quicksight-dashboard-geospatialstaticfilesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
