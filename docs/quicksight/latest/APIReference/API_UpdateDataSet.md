---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSet.html
---

# UpdateDataSet
<a name="API_UpdateDataSet"></a>

Updates a dataset. Partial updates are not supported by this operation.

## Request Syntax
<a name="API_UpdateDataSet_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}} HTTP/1.1
Content-type: application/json

{
   "ColumnGroups": [
      {
         "GeoSpatialColumnGroup": {
            "Columns": [ "{{string}}" ],
            "CountryCode": "{{string}}",
            "Name": "{{string}}"
         }
      }
   ],
   "ColumnLevelPermissionRules": [
      {
         "ColumnNames": [ "{{string}}" ],
         "Principals": [ "{{string}}" ]
      }
   ],
   "DataPrepConfiguration": {
      "DestinationTableMap": {
         "{{string}}" : {
            "Alias": "{{string}}",
            "Source": {
               "TransformOperationId": "{{string}}"
            }
         }
      },
      "SourceTableMap": {
         "{{string}}" : {
            "DataSet": {
               "DataSetArn": "{{string}}",
               "InputColumns": [
                  {
                     "Id": "{{string}}",
                     "Name": "{{string}}",
                     "SubType": "{{string}}",
                     "Type": "{{string}}"
                  }
               ]
            },
            "PhysicalTableId": "{{string}}"
         }
      },
      "TransformStepMap": {
         "{{string}}" : {
            "AggregateStep": {
               "Aggregations": [
                  {
                     "AggregationFunction": {
                        "ListAggregation": {
                           "Distinct": {{boolean}},
                           "InputColumnName": "{{string}}",
                           "Separator": "{{string}}"
                        },
                        "SimpleAggregation": {
                           "FunctionType": "{{string}}",
                           "InputColumnName": "{{string}}"
                        }
                     },
                     "NewColumnId": "{{string}}",
                     "NewColumnName": "{{string}}"
                  }
               ],
               "Alias": "{{string}}",
               "GroupByColumnNames": [ "{{string}}" ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "AppendStep": {
               "Alias": "{{string}}",
               "AppendedColumns": [
                  {
                     "ColumnName": "{{string}}",
                     "NewColumnId": "{{string}}"
                  }
               ],
               "FirstSource": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               },
               "SecondSource": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "CastColumnTypesStep": {
               "Alias": "{{string}}",
               "CastColumnTypeOperations": [
                  {
                     "ColumnName": "{{string}}",
                     "Format": "{{string}}",
                     "NewColumnType": "{{string}}",
                     "SubType": "{{string}}"
                  }
               ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "CreateColumnsStep": {
               "Alias": "{{string}}",
               "Columns": [
                  {
                     "ColumnId": "{{string}}",
                     "ColumnName": "{{string}}",
                     "Expression": "{{string}}"
                  }
               ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "FiltersStep": {
               "Alias": "{{string}}",
               "FilterOperations": [
                  {
                     "ConditionExpression": "{{string}}",
                     "DateFilterCondition": {
                        "ColumnName": "{{string}}",
                        "ComparisonFilterCondition": {
                           "Operator": "{{string}}",
                           "Value": {
                              "StaticValue": {{number}}
                           }
                        },
                        "RangeFilterCondition": {
                           "IncludeMaximum": {{boolean}},
                           "IncludeMinimum": {{boolean}},
                           "RangeMaximum": {
                              "StaticValue": {{number}}
                           },
                           "RangeMinimum": {
                              "StaticValue": {{number}}
                           }
                        }
                     },
                     "NumericFilterCondition": {
                        "ColumnName": "{{string}}",
                        "ComparisonFilterCondition": {
                           "Operator": "{{string}}",
                           "Value": {
                              "StaticValue": {{number}}
                           }
                        },
                        "RangeFilterCondition": {
                           "IncludeMaximum": {{boolean}},
                           "IncludeMinimum": {{boolean}},
                           "RangeMaximum": {
                              "StaticValue": {{number}}
                           },
                           "RangeMinimum": {
                              "StaticValue": {{number}}
                           }
                        }
                     },
                     "StringFilterCondition": {
                        "ColumnName": "{{string}}",
                        "ComparisonFilterCondition": {
                           "Operator": "{{string}}",
                           "Value": {
                              "StaticValue": "{{string}}"
                           }
                        },
                        "ListFilterCondition": {
                           "Operator": "{{string}}",
                           "Values": {
                              "StaticValues": [ "{{string}}" ]
                           }
                        }
                     }
                  }
               ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "ImportTableStep": {
               "Alias": "{{string}}",
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "SourceTableId": "{{string}}"
               }
            },
            "JoinStep": {
               "Alias": "{{string}}",
               "LeftOperand": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               },
               "LeftOperandProperties": {
                  "OutputColumnNameOverrides": [
                     {
                        "OutputColumnName": "{{string}}",
                        "SourceColumnName": "{{string}}"
                     }
                  ]
               },
               "OnClause": "{{string}}",
               "RightOperand": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               },
               "RightOperandProperties": {
                  "OutputColumnNameOverrides": [
                     {
                        "OutputColumnName": "{{string}}",
                        "SourceColumnName": "{{string}}"
                     }
                  ]
               },
               "Type": "{{string}}"
            },
            "PivotStep": {
               "Alias": "{{string}}",
               "GroupByColumnNames": [ "{{string}}" ],
               "PivotConfiguration": {
                  "LabelColumnName": "{{string}}",
                  "PivotedLabels": [
                     {
                        "LabelName": "{{string}}",
                        "NewColumnId": "{{string}}",
                        "NewColumnName": "{{string}}"
                     }
                  ]
               },
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               },
               "ValueColumnConfiguration": {
                  "AggregationFunction": {
                     "ListAggregation": {
                        "Distinct": {{boolean}},
                        "InputColumnName": "{{string}}",
                        "Separator": "{{string}}"
                     },
                     "SimpleAggregation": {
                        "FunctionType": "{{string}}",
                        "InputColumnName": "{{string}}"
                     }
                  }
               }
            },
            "ProjectStep": {
               "Alias": "{{string}}",
               "ProjectedColumns": [ "{{string}}" ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "RenameColumnsStep": {
               "Alias": "{{string}}",
               "RenameColumnOperations": [
                  {
                     "ColumnName": "{{string}}",
                     "NewColumnName": "{{string}}"
                  }
               ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               }
            },
            "UnpivotStep": {
               "Alias": "{{string}}",
               "ColumnsToUnpivot": [
                  {
                     "ColumnName": "{{string}}",
                     "NewValue": "{{string}}"
                  }
               ],
               "Source": {
                  "ColumnIdMappings": [
                     {
                        "SourceColumnId": "{{string}}",
                        "TargetColumnId": "{{string}}"
                     }
                  ],
                  "TransformOperationId": "{{string}}"
               },
               "UnpivotedLabelColumnId": "{{string}}",
               "UnpivotedLabelColumnName": "{{string}}",
               "UnpivotedValueColumnId": "{{string}}",
               "UnpivotedValueColumnName": "{{string}}"
            }
         }
      }
   },
   "DatasetParameters": [
      {
         "DateTimeDatasetParameter": {
            "DefaultValues": {
               "StaticValues": [ {{number}} ]
            },
            "Id": "{{string}}",
            "Name": "{{string}}",
            "TimeGranularity": "{{string}}",
            "ValueType": "{{string}}"
         },
         "DecimalDatasetParameter": {
            "DefaultValues": {
               "StaticValues": [ {{number}} ]
            },
            "Id": "{{string}}",
            "Name": "{{string}}",
            "ValueType": "{{string}}"
         },
         "IntegerDatasetParameter": {
            "DefaultValues": {
               "StaticValues": [ {{number}} ]
            },
            "Id": "{{string}}",
            "Name": "{{string}}",
            "ValueType": "{{string}}"
         },
         "StringDatasetParameter": {
            "DefaultValues": {
               "StaticValues": [ "{{string}}" ]
            },
            "Id": "{{string}}",
            "Name": "{{string}}",
            "ValueType": "{{string}}"
         }
      }
   ],
   "DataSetUsageConfiguration": {
      "DisableUseAsDirectQuerySource": {{boolean}},
      "DisableUseAsImportedSource": {{boolean}}
   },
   "FieldFolders": {
      "{{string}}" : {
         "columns": [ "{{string}}" ],
         "description": "{{string}}"
      }
   },
   "ImportMode": "{{string}}",
   "LogicalTableMap": {
      "{{string}}" : {
         "Alias": "{{string}}",
         "DataTransforms": [
            {
               "CastColumnTypeOperation": {
                  "ColumnName": "{{string}}",
                  "Format": "{{string}}",
                  "NewColumnType": "{{string}}",
                  "SubType": "{{string}}"
               },
               "CreateColumnsOperation": {
                  "Alias": "{{string}}",
                  "Columns": [
                     {
                        "ColumnId": "{{string}}",
                        "ColumnName": "{{string}}",
                        "Expression": "{{string}}"
                     }
                  ],
                  "Source": {
                     "ColumnIdMappings": [
                        {
                           "SourceColumnId": "{{string}}",
                           "TargetColumnId": "{{string}}"
                        }
                     ],
                     "TransformOperationId": "{{string}}"
                  }
               },
               "FilterOperation": {
                  "ConditionExpression": "{{string}}",
                  "DateFilterCondition": {
                     "ColumnName": "{{string}}",
                     "ComparisonFilterCondition": {
                        "Operator": "{{string}}",
                        "Value": {
                           "StaticValue": {{number}}
                        }
                     },
                     "RangeFilterCondition": {
                        "IncludeMaximum": {{boolean}},
                        "IncludeMinimum": {{boolean}},
                        "RangeMaximum": {
                           "StaticValue": {{number}}
                        },
                        "RangeMinimum": {
                           "StaticValue": {{number}}
                        }
                     }
                  },
                  "NumericFilterCondition": {
                     "ColumnName": "{{string}}",
                     "ComparisonFilterCondition": {
                        "Operator": "{{string}}",
                        "Value": {
                           "StaticValue": {{number}}
                        }
                     },
                     "RangeFilterCondition": {
                        "IncludeMaximum": {{boolean}},
                        "IncludeMinimum": {{boolean}},
                        "RangeMaximum": {
                           "StaticValue": {{number}}
                        },
                        "RangeMinimum": {
                           "StaticValue": {{number}}
                        }
                     }
                  },
                  "StringFilterCondition": {
                     "ColumnName": "{{string}}",
                     "ComparisonFilterCondition": {
                        "Operator": "{{string}}",
                        "Value": {
                           "StaticValue": "{{string}}"
                        }
                     },
                     "ListFilterCondition": {
                        "Operator": "{{string}}",
                        "Values": {
                           "StaticValues": [ "{{string}}" ]
                        }
                     }
                  }
               },
               "OverrideDatasetParameterOperation": {
                  "NewDefaultValues": {
                     "DateTimeStaticValues": [ {{number}} ],
                     "DecimalStaticValues": [ {{number}} ],
                     "IntegerStaticValues": [ {{number}} ],
                     "StringStaticValues": [ "{{string}}" ]
                  },
                  "NewParameterName": "{{string}}",
                  "ParameterName": "{{string}}"
               },
               "ProjectOperation": {
                  "Alias": "{{string}}",
                  "ProjectedColumns": [ "{{string}}" ],
                  "Source": {
                     "ColumnIdMappings": [
                        {
                           "SourceColumnId": "{{string}}",
                           "TargetColumnId": "{{string}}"
                        }
                     ],
                     "TransformOperationId": "{{string}}"
                  }
               },
               "RenameColumnOperation": {
                  "ColumnName": "{{string}}",
                  "NewColumnName": "{{string}}"
               },
               "TagColumnOperation": {
                  "ColumnName": "{{string}}",
                  "Tags": [
                     {
                        "ColumnDescription": {
                           "Text": "{{string}}"
                        },
                        "ColumnGeographicRole": "{{string}}"
                     }
                  ]
               },
               "UntagColumnOperation": {
                  "ColumnName": "{{string}}",
                  "TagNames": [ "{{string}}" ]
               }
            }
         ],
         "Source": {
            "DataSetArn": "{{string}}",
            "JoinInstruction": {
               "LeftJoinKeyProperties": {
                  "UniqueKey": {{boolean}}
               },
               "LeftOperand": "{{string}}",
               "OnClause": "{{string}}",
               "RightJoinKeyProperties": {
                  "UniqueKey": {{boolean}}
               },
               "RightOperand": "{{string}}",
               "Type": "{{string}}"
            },
            "PhysicalTableId": "{{string}}"
         }
      }
   },
   "Name": "{{string}}",
   "PerformanceConfiguration": {
      "UniqueKeys": [
         {
            "ColumnNames": [ "{{string}}" ]
         }
      ]
   },
   "PhysicalTableMap": {
      "{{string}}" : {
         "CustomSql": {
            "Columns": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}",
                  "SubType": "{{string}}",
                  "Type": "{{string}}"
               }
            ],
            "DataSourceArn": "{{string}}",
            "Name": "{{string}}",
            "SqlQuery": "{{string}}"
         },
         "FileSource": {
            "DataSourceArn": "{{string}}",
            "InputColumns": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}",
                  "SubType": "{{string}}",
                  "Type": "{{string}}"
               }
            ],
            "SheetIndex": {{number}},
            "UploadSettings": {
               "ContainsHeader": {{boolean}},
               "CustomCellAddressRange": "{{string}}",
               "Delimiter": "{{string}}",
               "Format": "{{string}}",
               "StartFromRow": {{number}},
               "TextQualifier": "{{string}}"
            }
         },
         "RelationalTable": {
            "Catalog": "{{string}}",
            "DataSourceArn": "{{string}}",
            "InputColumns": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}",
                  "SubType": "{{string}}",
                  "Type": "{{string}}"
               }
            ],
            "Name": "{{string}}",
            "Schema": "{{string}}"
         },
         "S3Source": {
            "DataSourceArn": "{{string}}",
            "InputColumns": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}",
                  "SubType": "{{string}}",
                  "Type": "{{string}}"
               }
            ],
            "UploadSettings": {
               "ContainsHeader": {{boolean}},
               "CustomCellAddressRange": "{{string}}",
               "Delimiter": "{{string}}",
               "Format": "{{string}}",
               "StartFromRow": {{number}},
               "TextQualifier": "{{string}}"
            }
         },
         "SaaSTable": {
            "DataSourceArn": "{{string}}",
            "InputColumns": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}",
                  "SubType": "{{string}}",
                  "Type": "{{string}}"
               }
            ],
            "TablePath": [
               {
                  "Id": "{{string}}",
                  "Name": "{{string}}"
               }
            ]
         }
      }
   },
   "RowLevelPermissionDataSet": {
      "Arn": "{{string}}",
      "FormatVersion": "{{string}}",
      "Namespace": "{{string}}",
      "PermissionPolicy": "{{string}}",
      "Status": "{{string}}"
   },
   "RowLevelPermissionTagConfiguration": {
      "Status": "{{string}}",
      "TagRuleConfigurations": [
         [ "{{string}}" ]
      ],
      "TagRules": [
         {
            "ColumnName": "{{string}}",
            "MatchAllValue": "{{string}}",
            "TagKey": "{{string}}",
            "TagMultiValueDelimiter": "{{string}}"
         }
      ]
   },
   "SemanticModelConfiguration": {
      "SemanticMetadata": [
         {
            "CustomInstructions": [
               {
                  "InlineCustomInstruction": {
                     "InstructionText": "{{string}}",
                     "UploadedDocumentMetadata": {
                        "Name": "{{string}}"
                     }
                  }
               }
            ],
            "Description": {
               "Text": "{{string}}"
            }
         }
      ],
      "TableMap": {
         "{{string}}" : {
            "Alias": "{{string}}",
            "DestinationTableId": "{{string}}",
            "RowLevelPermissionConfiguration": {
               "RowLevelPermissionDataSet": {
                  "Arn": "{{string}}",
                  "FormatVersion": "{{string}}",
                  "Namespace": "{{string}}",
                  "PermissionPolicy": "{{string}}",
                  "Status": "{{string}}"
               },
               "TagConfiguration": {
                  "Status": "{{string}}",
                  "TagRuleConfigurations": [
                     [ "{{string}}" ]
                  ],
                  "TagRules": [
                     {
                        "ColumnName": "{{string}}",
                        "MatchAllValue": "{{string}}",
                        "TagKey": "{{string}}",
                        "TagMultiValueDelimiter": "{{string}}"
                     }
                  ]
               }
            },
            "SemanticMetadata": {
               "ColumnMetadata": [
                  {
                     "ColumnNames": [ "{{string}}" ],
                     "ColumnProperties": [
                        {
                           "AdditionalNotes": {
                              "Text": "{{string}}"
                           },
                           "Description": {
                              "Text": "{{string}}"
                           },
                           "SemanticType": {
                              "GeographicalRole": "{{string}}"
                           }
                        }
                     ]
                  }
               ]
            }
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DataSetId](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-uri-DataSetId"></a>
The ID for the dataset that you want to update. This ID is unique per AWS Region for each AWS account.
Required: Yes

## Request Body
<a name="API_UpdateDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ImportMode](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-ImportMode"></a>
Indicates whether you want to import the data into SPICE.
Type: String
Valid Values: `SPICE | DIRECT_QUERY`
Required: Yes

 ** [Name](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-Name"></a>
The display name for the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [PhysicalTableMap](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-PhysicalTableMap"></a>
Declares the physical tables that are available in the underlying data sources.
Type: String to [PhysicalTable](API_PhysicalTable.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** [ColumnGroups](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-ColumnGroups"></a>
Groupings of columns that work together in certain Amazon Quick Sight features. Currently, only geospatial hierarchy is supported.
Type: Array of [ColumnGroup](API_ColumnGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: No

 ** [ColumnLevelPermissionRules](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-ColumnLevelPermissionRules"></a>
A set of one or more definitions of a ` [ColumnLevelPermissionRule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html) `.
Type: Array of [ColumnLevelPermissionRule](API_ColumnLevelPermissionRule.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [DataPrepConfiguration](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-DataPrepConfiguration"></a>
The data preparation configuration for the dataset. This configuration defines the source tables, transformation steps, and destination tables used to prepare the data. Required when using the new data preparation experience.
Type: [DataPrepConfiguration](API_DataPrepConfiguration.md) object
Required: No

 ** [DatasetParameters](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-DatasetParameters"></a>
The parameter declarations of the dataset.
Type: Array of [DatasetParameter](API_DatasetParameter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** [DataSetUsageConfiguration](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-DataSetUsageConfiguration"></a>
The usage configuration to apply to child datasets that reference this dataset as a source.
Type: [DataSetUsageConfiguration](API_DataSetUsageConfiguration.md) object
Required: No

 ** [FieldFolders](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-FieldFolders"></a>
The folder that contains fields and nested subfolders for your dataset.
Type: String to [FieldFolder](API_FieldFolder.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [LogicalTableMap](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-LogicalTableMap"></a>
 *This parameter has been deprecated.*
Configures the combination and transformation of the data from the physical tables. This parameter is used with the legacy data preparation experience.
Type: String to [LogicalTable](API_LogicalTable.md) object map
Map Entries: Maximum number of 64 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: No

 ** [PerformanceConfiguration](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-PerformanceConfiguration"></a>
The configuration for the performance optimization of the dataset that contains a `UniqueKey` configuration.
Type: [PerformanceConfiguration](API_PerformanceConfiguration.md) object
Required: No

 ** [RowLevelPermissionDataSet](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-RowLevelPermissionDataSet"></a>
 *This parameter has been deprecated.*
The row-level security configuration for the data you want to create. This parameter is used with the legacy data preparation experience.
Type: [RowLevelPermissionDataSet](API_RowLevelPermissionDataSet.md) object
Required: No

 ** [RowLevelPermissionTagConfiguration](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-RowLevelPermissionTagConfiguration"></a>
 *This parameter has been deprecated.*
The configuration of tags on a dataset to set row-level security. Row-level security tags are currently supported for anonymous embedding only. This parameter is used with the legacy data preparation experience.
Type: [RowLevelPermissionTagConfiguration](API_RowLevelPermissionTagConfiguration.md) object
Required: No

 ** [SemanticModelConfiguration](#API_UpdateDataSet_RequestSyntax) **   <a name="QS-UpdateDataSet-request-SemanticModelConfiguration"></a>
The semantic model configuration for the dataset. This configuration defines how the prepared data is structured for an analysis, including table mappings and row-level security configurations. Required when using the new data preparation experience.
Type: [SemanticModelConfiguration](API_SemanticModelConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataSet_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "DataSetId": "string",
   "IngestionArn": "string",
   "IngestionId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDataSet_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-Arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String

 ** [DataSetId](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-DataSetId"></a>
The ID for the dataset that you want to update. This ID is unique per AWS Region for each AWS account.
Type: String

 ** [IngestionArn](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-IngestionArn"></a>
The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
Type: String

 ** [IngestionId](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-IngestionId"></a>
The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
Type: String

 ** [RequestId](#API_UpdateDataSet_ResponseSyntax) **   <a name="QS-UpdateDataSet-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDataSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidDataSetParameterValueException **
An exception thrown when an invalid parameter value is provided for dataset operations.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## Examples
<a name="API_UpdateDataSet_Examples"></a>

### Example
<a name="API_UpdateDataSet_Example_1"></a>

This example illustrates one usage of UpdateDataSet.

#### Sample Request
<a name="API_UpdateDataSet_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/data-sets/{DataSetId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDataSet)
