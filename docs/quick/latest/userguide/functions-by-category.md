---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/functions-by-category.html
---

# Functions by category
<a name="functions-by-category"></a>

In this section, you can find a list of the functions available in Amazon Quick, sorted by category.

**Topics**
+ [Aggregate functions](#aggregate-functions)
+ [Conditional functions](#conditional-functions)
+ [Date functions](#date-functions)
+ [Numeric functions](#numeric-functions)
+ [Mathematical functions](#mathematical-functions)
+ [String functions](#string-functions)
+ [Table calculations](#table-calculations)

## Aggregate functions
<a name="aggregate-functions"></a>

The aggregate functions for calculated fields in Amazon Quick include the following. These are only available during analysis and visualization. Each of these functions returns values grouped by the chosen dimension or dimensions. For each aggregation, there is also a conditional aggregation. These perform the same type of aggregation, based on a condition.
+ [https://docs.aws.amazon.com/quicksight/latest/user/avg-function.html](https://docs.aws.amazon.com/quicksight/latest/user/avg-function.html) averages the set of numbers in the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/avgIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/avgIf-function.html) calculates the average based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/count-function.html](https://docs.aws.amazon.com/quicksight/latest/user/count-function.html) calculates the number of values in a dimension or measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/countIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/countIf-function.html) calculates the count based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/distinct_count-function.html](https://docs.aws.amazon.com/quicksight/latest/user/distinct_count-function.html) calculates the number of distinct values in a dimension or measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/distinct_countIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/distinct_countIf-function.html) calculates the distinct count based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/max-function.html](https://docs.aws.amazon.com/quicksight/latest/user/max-function.html) returns the maximum value of the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/maxIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/maxIf-function.html) calculates the maximum based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/median-function.html](https://docs.aws.amazon.com/quicksight/latest/user/median-function.html) returns the median value of the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/medianIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/medianIf-function.html) calculates the median based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/min-function.html](https://docs.aws.amazon.com/quicksight/latest/user/min-function.html) returns the minimum value of the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/minIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/minIf-function.html) calculates the minimum based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentile-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentile-function.html) (alias of `percentileDisc`) computes the *n*th percentile of the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentileCont-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentileCont-function.html) calculates the *n*th percentile based on a continuous distribution of the numbers of the specified measure, grouped by the chosen dimension or dimensions.
+ [percentileDisc (percentile)](https://docs.aws.amazon.com/quicksight/latest/user/percentileDisc-function.html) calculates the *n*th percentile based on the actual numbers of the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvg-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvg-function.html) averages the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCount-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCount-function.html) calculates the number of values in a dimension or measure for a given time granularity (for instance, Quarter) up to a point in time including duplicates.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMax-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMax-function.html) returns the maximum value of the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMedian-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMedian-function.html) returns the median value of the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMin-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMin-function.html) returns the minimum value of the specified measure or date for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentile-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentile-function.html) calculates the percentile based on the actual numbers in measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentileCont-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentileCont-function.html) calculates percentile based on a continuous distribution of the numbers in the measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDev-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDev-function.html) calculates the standard deviation of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDevP-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDevP-function.html) calculates the population standard deviation of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSum-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSum-function.html) adds the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVar-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVar-function.html) calculates the sample variance of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVarP-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVarP-function.html) calculates the population variance of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdev-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdev-function.html)) calculates the standard deviation of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdevIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdevIf-function.html) calculates the sample standard deviation based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdevp-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdevp-function.html) calculates the standard deviation of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a biased population.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdevpIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdevpIf-function.html) calculates the population deviation based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/var-function.html](https://docs.aws.amazon.com/quicksight/latest/user/var-function.html)) calculates the variance of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/varIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/varIf-function.html) calculates the sample variance based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/varp-function.html](https://docs.aws.amazon.com/quicksight/latest/user/varp-function.html)) calculates the variance of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a biased population.
+ [https://docs.aws.amazon.com/quicksight/latest/user/varpIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/varpIf-function.html) calculates the population variance based on a conditional statement.
+ [https://docs.aws.amazon.com/quicksight/latest/user/sum-function.html](https://docs.aws.amazon.com/quicksight/latest/user/sum-function.html)) adds the set of numbers in the specified measure, grouped by the chosen dimension or dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/sumIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/sumIf-function.html)) calculates the sum based on a conditional statement.

## Conditional functions
<a name="conditional-functions"></a>

The conditional functions for calculated fields in Amazon Quick include the following:
+ [https://docs.aws.amazon.com/quicksight/latest/user/coalesce-function.html](https://docs.aws.amazon.com/quicksight/latest/user/coalesce-function.html) returns the value of the first argument that is not null.
+ [https://docs.aws.amazon.com/quicksight/latest/user/ifelse-function.html](https://docs.aws.amazon.com/quicksight/latest/user/ifelse-function.html) evaluates a set of *if*, *then* expression pairings, and returns the value of the *then* argument for the first *if* argument that evaluates to true.
+ [https://docs.aws.amazon.com/quicksight/latest/user/in-function.html](https://docs.aws.amazon.com/quicksight/latest/user/in-function.html) evaluates an expression to see if it is in a given list of values.
+ [https://docs.aws.amazon.com/quicksight/latest/user/isNotNull-function.html](https://docs.aws.amazon.com/quicksight/latest/user/isNotNull-function.html) evaluates an expression to see if it is not null.
+ [https://docs.aws.amazon.com/quicksight/latest/user/isNull-function.html](https://docs.aws.amazon.com/quicksight/latest/user/isNull-function.html) evaluates an expression to see if it is null. If the expression is null, `isNull` returns true, and otherwise it returns false.
+ [https://docs.aws.amazon.com/quicksight/latest/user/notIn-function.html](https://docs.aws.amazon.com/quicksight/latest/user/notIn-function.html) evaluates an expression to see if it is not in a given list of values.
+ [https://docs.aws.amazon.com/quicksight/latest/user/nullIf-function.html](https://docs.aws.amazon.com/quicksight/latest/user/nullIf-function.html) compares two expressions. If they are equal, the function returns null. If they are not equal, the function returns the first expression.
+ [https://docs.aws.amazon.com/quicksight/latest/user/switch-function.html](https://docs.aws.amazon.com/quicksight/latest/user/switch-function.html) returns an expression that matches the first label equal to the condition expression.

## Date functions
<a name="date-functions"></a>

The date functions for calculated fields in Amazon Quick include the following:
+ [https://docs.aws.amazon.com/quicksight/latest/user/addDateTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/addDateTime-function.html) adds or subtracts a unit of time to the date or time provided.
+ [https://docs.aws.amazon.com/quicksight/latest/user/addWorkDays-function.html](https://docs.aws.amazon.com/quicksight/latest/user/addWorkDays-function.html) adds or subtracts the given number of work days to the date or time provided.
+ [https://docs.aws.amazon.com/quicksight/latest/user/dateDiff-function.html](https://docs.aws.amazon.com/quicksight/latest/user/dateDiff-function.html) returns the difference in days between two date fields.
+ [https://docs.aws.amazon.com/quicksight/latest/user/epochDate-function.html](https://docs.aws.amazon.com/quicksight/latest/user/epochDate-function.html) converts an epoch date into a standard date.
+ [https://docs.aws.amazon.com/quicksight/latest/user/extract-function.html](https://docs.aws.amazon.com/quicksight/latest/user/extract-function.html) returns a specified portion of a date value.
+ [https://docs.aws.amazon.com/quicksight/latest/user/formatDate-function.html](https://docs.aws.amazon.com/quicksight/latest/user/formatDate-function.html) formats a date using a pattern you specify.
+ [https://docs.aws.amazon.com/quicksight/latest/user/isWorkDay-function.html](https://docs.aws.amazon.com/quicksight/latest/user/isWorkDay-function.html) returns TRUE if a given date-time value is a work or business day.
+ [https://docs.aws.amazon.com/quicksight/latest/user/netWorkDays-function.html](https://docs.aws.amazon.com/quicksight/latest/user/netWorkDays-function.html) returns the number of working days between the provided two date values.
+ [https://docs.aws.amazon.com/quicksight/latest/user/now-function.html](https://docs.aws.amazon.com/quicksight/latest/user/now-function.html) returns the current date and time, using either settings for a database, or UTC for file and Salesforce.
+ [https://docs.aws.amazon.com/quicksight/latest/user/truncDate-function.html](https://docs.aws.amazon.com/quicksight/latest/user/truncDate-function.html) returns a date value that represents a specified portion of a date.

## Numeric functions
<a name="numeric-functions"></a>

The numeric functions for calculated fields in Amazon Quick include the following:
+ [https://docs.aws.amazon.com/quicksight/latest/user/ceil-function.html](https://docs.aws.amazon.com/quicksight/latest/user/ceil-function.html) rounds a decimal value to the next highest integer.
+ [https://docs.aws.amazon.com/quicksight/latest/user/decimalToInt-function.html](https://docs.aws.amazon.com/quicksight/latest/user/decimalToInt-function.html) converts a decimal value to an integer.
+ [https://docs.aws.amazon.com/quicksight/latest/user/floor-function.html](https://docs.aws.amazon.com/quicksight/latest/user/floor-function.html) decrements a decimal value to the next lowest integer.
+ [https://docs.aws.amazon.com/quicksight/latest/user/intToDecimal-function.html](https://docs.aws.amazon.com/quicksight/latest/user/intToDecimal-function.html) converts an integer value to a decimal.
+ [https://docs.aws.amazon.com/quicksight/latest/user/round-function.html](https://docs.aws.amazon.com/quicksight/latest/user/round-function.html) rounds a decimal value to the closest integer or, if scale is specified, to the closest decimal place.

## Mathematical functions
<a name="mathematical-functions"></a>

The mathematical functions for calculated fields in Amazon Quick include the following:
+ `[https://docs.aws.amazon.com/quicksight/latest/user/mod-function.html](https://docs.aws.amazon.com/quicksight/latest/user/mod-function.html)({{number}}, {{divisor}})` – Finds the remainder after dividing a number by a divisor.
+ `[https://docs.aws.amazon.com/quicksight/latest/user/log-function.html](https://docs.aws.amazon.com/quicksight/latest/user/log-function.html)({{expression}}) `– Returns the base 10 logarithm of a given expression.
+ `[https://docs.aws.amazon.com/quicksight/latest/user/ln-function.html](https://docs.aws.amazon.com/quicksight/latest/user/ln-function.html)({{expression}}) `– Returns the natural logarithm of a given expression.
+ `[https://docs.aws.amazon.com/quicksight/latest/user/abs-function.html](https://docs.aws.amazon.com/quicksight/latest/user/abs-function.html)({{expression}}) `– Returns the absolute value of a given expression.
+ `[https://docs.aws.amazon.com/quicksight/latest/user/sqrt-function.html](https://docs.aws.amazon.com/quicksight/latest/user/sqrt-function.html)({{expression}}) `– Returns the square root of a given expression.
+ `[https://docs.aws.amazon.com/quicksight/latest/user/exp-function.html](https://docs.aws.amazon.com/quicksight/latest/user/exp-function.html)({{expression}}) `– Returns the base of natural log *e* raised to the power of a given expression.

## String functions
<a name="string-functions"></a>

The string (text) functions for calculated fields in Amazon Quick include the following:
+ [https://docs.aws.amazon.com/quicksight/latest/user/concat-function.html](https://docs.aws.amazon.com/quicksight/latest/user/concat-function.html) concatenates two or more strings.
+ [https://docs.aws.amazon.com/quicksight/latest/user/contains-function.html](https://docs.aws.amazon.com/quicksight/latest/user/contains-function.html) checks if an expression contains a substring.
+ [https://docs.aws.amazon.com/quicksight/latest/user/endsWith-function.html](https://docs.aws.amazon.com/quicksight/latest/user/endsWith-function.html) checks if the expression ends with the substring specified.
+ [https://docs.aws.amazon.com/quicksight/latest/user/left-function.html](https://docs.aws.amazon.com/quicksight/latest/user/left-function.html) returns the specified number of leftmost characters from a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/locate-function.html](https://docs.aws.amazon.com/quicksight/latest/user/locate-function.html) locates a substring within another string, and returns the number of characters before the substring.
+ [https://docs.aws.amazon.com/quicksight/latest/user/ltrim-function.html](https://docs.aws.amazon.com/quicksight/latest/user/ltrim-function.html) removes preceding blank space from a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/parseDate-function.html](https://docs.aws.amazon.com/quicksight/latest/user/parseDate-function.html) parses a string to determine if it contains a date value, and returns the date if found.
+ [https://docs.aws.amazon.com/quicksight/latest/user/parseDecimal-function.html](https://docs.aws.amazon.com/quicksight/latest/user/parseDecimal-function.html) parses a string to determine if it contains a decimal value.
+ [https://docs.aws.amazon.com/quicksight/latest/user/parseInt-function.html](https://docs.aws.amazon.com/quicksight/latest/user/parseInt-function.html) parses a string to determine if it contains an integer value.
+ [https://docs.aws.amazon.com/quicksight/latest/user/parseJson-function.html](https://docs.aws.amazon.com/quicksight/latest/user/parseJson-function.html) parses values from a native JSON or from a JSON object in a text field.
+ [https://docs.aws.amazon.com/quicksight/latest/user/replace-function.html](https://docs.aws.amazon.com/quicksight/latest/user/replace-function.html) replaces part of a string with a new string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/right-function.html](https://docs.aws.amazon.com/quicksight/latest/user/right-function.html) returns the specified number of rightmost characters from a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/rtrim-function.html](https://docs.aws.amazon.com/quicksight/latest/user/rtrim-function.html) removes following blank space from a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/split-function.html](https://docs.aws.amazon.com/quicksight/latest/user/split-function.html) splits a string into an array of substrings, based on a delimiter that you choose, and returns the item specified by the position.
+ [https://docs.aws.amazon.com/quicksight/latest/user/startsWith-function.html](https://docs.aws.amazon.com/quicksight/latest/user/startsWith-function.html) checks if the expression starts with the substring specified.
+ [https://docs.aws.amazon.com/quicksight/latest/user/strlen-function.html](https://docs.aws.amazon.com/quicksight/latest/user/strlen-function.html) returns the number of characters in a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/substring-function.html](https://docs.aws.amazon.com/quicksight/latest/user/substring-function.html) returns the specified number of characters in a string, starting at the specified location.
+ [https://docs.aws.amazon.com/quicksight/latest/user/toLower-function.html](https://docs.aws.amazon.com/quicksight/latest/user/toLower-function.html) formats a string in all lowercase.
+ [https://docs.aws.amazon.com/quicksight/latest/user/toString-function.html](https://docs.aws.amazon.com/quicksight/latest/user/toString-function.html) formats the input expression as a string.
+ [https://docs.aws.amazon.com/quicksight/latest/user/toUpper-function.html](https://docs.aws.amazon.com/quicksight/latest/user/toUpper-function.html) formats a string in all uppercase.
+ [https://docs.aws.amazon.com/quicksight/latest/user/trim-function.html](https://docs.aws.amazon.com/quicksight/latest/user/trim-function.html) removes both preceding and following blank space from a string.

## Table calculations
<a name="table-calculations"></a>

Table calculations form a group of functions that provide context in an analysis. They provide support for enriched aggregated analysis. By using these calculations, you can address common business scenarios such as calculating percentage of total, running sum, difference, common baseline, and rank.

When you are analyzing data in a specific visual, you can apply table calculations to the current set of data to discover how dimensions influence measures or each other. Visualized data is your result set based on your current dataset, with all the filters, field selections, and customizations applied. To see exactly what this result set is, you can export your visual to a file. A table calculation function performs operations on the data to reveal relationships between fields.

**Lookup-based functions**
+ [https://docs.aws.amazon.com/quicksight/latest/user/difference-function.html](https://docs.aws.amazon.com/quicksight/latest/user/difference-function.html) calculates the difference between a measure based on one set of partitions and sorts, and a measure based on another.
+ [https://docs.aws.amazon.com/quicksight/latest/user/lag-function.html](https://docs.aws.amazon.com/quicksight/latest/user/lag-function.html) calculates the lag (previous) value for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/lead-function.html](https://docs.aws.amazon.com/quicksight/latest/user/lead-function.html) calculates the lead (following) value for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentDifference-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentDifference-function.html) calculates the percentage difference between the current value and a comparison value.

**Over functions**
+ [https://docs.aws.amazon.com/quicksight/latest/user/avgOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/avgOver-function.html) calculates the average of a measure over one or more dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/countOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/countOver-function.html) calculates the count of a field over one or more dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/distinctCountOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/distinctCountOver-function.html) calculates the distinct count of the operand partitioned by the specified attributes at a specified level.
+ [https://docs.aws.amazon.com/quicksight/latest/user/maxOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/maxOver-function.html) calculates the maximum of a measure over one or more dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/minOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/minOver-function.html) the minimum of a measure over one or more dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentileOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentileOver-function.html) (alias of `percentileDiscOver`) calculates the *n*th percentile of a measure partitioned by a list of dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentileContOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentileContOver-function.html) calculates the *n*th percentile based on a continuous distribution of the numbers of a measure partitioned by a list of dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentileDiscOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentileDiscOver-function.html) calculates the *n*th percentile based on the actual numbers of a measure partitioned by a list of dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentOfTotal-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentOfTotal-function.html) calculates the percentage that a measure contributes to the total.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodDifference-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodDifference-function.html) calculates the difference of a measure over two different time periods as specified by period granularity and offset.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodLastValue-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodLastValue-function.html) calculates the last (previous) value of a measure from a previous time period as specified by period granularity and offset.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodPercentDifference-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodPercentDifference-function.html) calculates the percent difference of a measure over two different time periods as specified by period granularity and offset.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvgOverTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvgOverTime-function.html) calculates the average of a measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCountOverTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCountOverTime-function.html) calculates the count of a dimension or measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMaxOverTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMaxOverTime-function.html) calculates the maximum of a measure or date for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMinOverTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMinOverTime-function.html) calculates the minimum of a measure or date for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSumOverTime-function.html](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSumOverTime-function.html) calculates the sum of a measure for a given time granularity (for instance, a quarter) up to a point in time.
+ [https://docs.aws.amazon.com/quicksight/latest/user/sumOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/sumOver-function.html) calculates the sum of a measure over one or more dimensions.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdevOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdevOver-function.html) calculates the standard deviation of the specified measure, partitioned by the chosen attribute or attributes, based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/stdevpOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/stdevpOver-function.html) calculates the standard deviation of the specified measure, partitioned by the chosen attribute or attributes, based on a biased population.
+ [https://docs.aws.amazon.com/quicksight/latest/user/varOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/varOver-function.html) calculates the variance of the specified measure, partitioned by the chosen attribute or attributes, based on a sample.
+ [https://docs.aws.amazon.com/quicksight/latest/user/varpOver-function.html](https://docs.aws.amazon.com/quicksight/latest/user/varpOver-function.html) calculates the variance of the specified measure, partitioned by the chosen attribute or attributes, based on a biased population.

**Ranking functions**
+ [https://docs.aws.amazon.com/quicksight/latest/user/rank-function.html](https://docs.aws.amazon.com/quicksight/latest/user/rank-function.html) calculates the rank of a measure or a dimension.
+ [https://docs.aws.amazon.com/quicksight/latest/user/denseRank-function.html](https://docs.aws.amazon.com/quicksight/latest/user/denseRank-function.html) calculates the rank of a measure or a dimension, ignoring duplicates.
+ [https://docs.aws.amazon.com/quicksight/latest/user/percentileRank-function.html](https://docs.aws.amazon.com/quicksight/latest/user/percentileRank-function.html) calculates the rank of a measure or a dimension, based on percentile.

**Running functions**
+ [https://docs.aws.amazon.com/quicksight/latest/user/runningAvg-function.html](https://docs.aws.amazon.com/quicksight/latest/user/runningAvg-function.html) calculates a running average for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/runningCount-function.html](https://docs.aws.amazon.com/quicksight/latest/user/runningCount-function.html) calculates a running count for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/runningMax-function.html](https://docs.aws.amazon.com/quicksight/latest/user/runningMax-function.html) calculates a running maximum for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/runningMin-function.html](https://docs.aws.amazon.com/quicksight/latest/user/runningMin-function.html) calculates a running minimum for a measure.
+ [https://docs.aws.amazon.com/quicksight/latest/user/runningSum-function.html](https://docs.aws.amazon.com/quicksight/latest/user/runningSum-function.html) calculates a running sum for a measure.

**Window functions**
+ [https://docs.aws.amazon.com/quicksight/latest/user/firstValue-function.html](https://docs.aws.amazon.com/quicksight/latest/user/firstValue-function.html) calculates the first value of the aggregated measure or dimension partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/lastValue-function.html](https://docs.aws.amazon.com/quicksight/latest/user/lastValue-function.html) calculates the last value of the aggregated measure or dimension partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/windowAvg-function.html](https://docs.aws.amazon.com/quicksight/latest/user/windowAvg-function.html) calculates the average of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/windowCount-function.html](https://docs.aws.amazon.com/quicksight/latest/user/windowCount-function.html) calculates the count of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/windowMax-function.html](https://docs.aws.amazon.com/quicksight/latest/user/windowMax-function.html) calculates the maximum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/windowMin-function.html](https://docs.aws.amazon.com/quicksight/latest/user/windowMin-function.html) calculates the minimum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
+ [https://docs.aws.amazon.com/quicksight/latest/user/windowSum-function.html](https://docs.aws.amazon.com/quicksight/latest/user/windowSum-function.html) calculates the sum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
