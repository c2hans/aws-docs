---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/converters.html
---

# Converters

In some cases, you might have to modify or transform data while saving or reading from the DynamoDB database. In those scenarios, you can use the [IPropertyConverter](https://docs.aws.amazon.com/sdkfornet1/latest/apidocs/html/T_Amazon_DynamoDBv2_DataModel_IPropertyConverter.htm) interface of the [Amazon.DynamoDBv2.DataModel](https://docs.aws.amazon.com/sdkfornet1/latest/apidocs/html/N_Amazon_DynamoDBv2_DataModel.htm) namespace, by using code similar to the following:

```
   // Converts the null values of a string property to a valid string and vice versa.
    public class NullOrStringConverter : IPropertyConverter
    {
        // Called when creating the JSON / DynamoDB item from the model
        public DynamoDBEntry ToEntry(object value)
        {
            var entry = new Primitive
            {
                  value = new DynamoDBNull()
            };
            if(value != null)
            {
                  entry.Value = value.ToString();
            }
            return entry;
        }
       // Called when populating the model from the JSON / DynamoDB item
        public object FromEntry(DynamoDBEntry entry)
        {
            if(entry is DynamoDBNull)
            {
                  return string.Empty;
            }
            else
            {
                  return entry.ToString();
            }
        }
    }
```

Converter usage in the model:

```
[DynamoDBTable("AppLibrary")]
public class ProdApp
{
        . . .

        [DynamoDBProperty (typeof(NullOrString))]
        public string AppConfigId { get; set; }
         . . .
}
```
