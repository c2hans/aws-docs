---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-forecastcomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ForecastComputation
<a name="aws-properties-quicksight-dashboard-forecastcomputation"></a>

The forecast computation configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-forecastcomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-forecastcomputation-syntax.json"></a>

```
{
  "[ComputationId](#cfn-quicksight-dashboard-forecastcomputation-computationid)" : {{String}},
  "[CustomSeasonalityValue](#cfn-quicksight-dashboard-forecastcomputation-customseasonalityvalue)" : {{Number}},
  "[LowerBoundary](#cfn-quicksight-dashboard-forecastcomputation-lowerboundary)" : {{Number}},
  "[Name](#cfn-quicksight-dashboard-forecastcomputation-name)" : {{String}},
  "[PeriodsBackward](#cfn-quicksight-dashboard-forecastcomputation-periodsbackward)" : {{Number}},
  "[PeriodsForward](#cfn-quicksight-dashboard-forecastcomputation-periodsforward)" : {{Number}},
  "[PredictionInterval](#cfn-quicksight-dashboard-forecastcomputation-predictioninterval)" : {{Number}},
  "[Seasonality](#cfn-quicksight-dashboard-forecastcomputation-seasonality)" : {{String}},
  "[Time](#cfn-quicksight-dashboard-forecastcomputation-time)" : {{DimensionField}},
  "[UpperBoundary](#cfn-quicksight-dashboard-forecastcomputation-upperboundary)" : {{Number}},
  "[Value](#cfn-quicksight-dashboard-forecastcomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-forecastcomputation-syntax.yaml"></a>

```
  [ComputationId](#cfn-quicksight-dashboard-forecastcomputation-computationid): {{String}}
  [CustomSeasonalityValue](#cfn-quicksight-dashboard-forecastcomputation-customseasonalityvalue): {{Number}}
  [LowerBoundary](#cfn-quicksight-dashboard-forecastcomputation-lowerboundary): {{Number}}
  [Name](#cfn-quicksight-dashboard-forecastcomputation-name): {{String}}
  [PeriodsBackward](#cfn-quicksight-dashboard-forecastcomputation-periodsbackward): {{Number}}
  [PeriodsForward](#cfn-quicksight-dashboard-forecastcomputation-periodsforward): {{Number}}
  [PredictionInterval](#cfn-quicksight-dashboard-forecastcomputation-predictioninterval): {{Number}}
  [Seasonality](#cfn-quicksight-dashboard-forecastcomputation-seasonality): {{String}}
  [Time](#cfn-quicksight-dashboard-forecastcomputation-time): {{
    DimensionField}}
  [UpperBoundary](#cfn-quicksight-dashboard-forecastcomputation-upperboundary): {{Number}}
  [Value](#cfn-quicksight-dashboard-forecastcomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-forecastcomputation-properties"></a>

`ComputationId`  <a name="cfn-quicksight-dashboard-forecastcomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSeasonalityValue`  <a name="cfn-quicksight-dashboard-forecastcomputation-customseasonalityvalue"></a>
The custom seasonality value setup of a forecast computation.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `180`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LowerBoundary`  <a name="cfn-quicksight-dashboard-forecastcomputation-lowerboundary"></a>
The lower boundary setup of a forecast computation.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-forecastcomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeriodsBackward`  <a name="cfn-quicksight-dashboard-forecastcomputation-periodsbackward"></a>
The periods backward setup of a forecast computation.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeriodsForward`  <a name="cfn-quicksight-dashboard-forecastcomputation-periodsforward"></a>
The periods forward setup of a forecast computation.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredictionInterval`  <a name="cfn-quicksight-dashboard-forecastcomputation-predictioninterval"></a>
The prediction interval setup of a forecast computation.
*Required*: No
*Type*: Number
*Minimum*: `50`
*Maximum*: `95`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Seasonality`  <a name="cfn-quicksight-dashboard-forecastcomputation-seasonality"></a>
The seasonality setup of a forecast computation. Choose one of the following options:
+  `AUTOMATIC`
+ `CUSTOM`: Checks the custom seasonality value.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-quicksight-dashboard-forecastcomputation-time"></a>
The time field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpperBoundary`  <a name="cfn-quicksight-dashboard-forecastcomputation-upperboundary"></a>
The upper boundary setup of a forecast computation.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dashboard-forecastcomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
