---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRetainRule.html
---

# CrossRegionCopyRetainRule
<a name="API_CrossRegionCopyRetainRule"></a>

Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies. After the retention period expires, the cross-Region copy is deleted.

## Contents
<a name="API_CrossRegionCopyRetainRule_Contents"></a>

 ** Interval **   <a name="dlm-Type-CrossRegionCopyRetainRule-Interval"></a>
The amount of time to retain a cross-Region snapshot or AMI copy. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-CrossRegionCopyRetainRule-IntervalUnit"></a>
The unit of time for time-based retention. For example, to retain a cross-Region copy for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS`.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_CrossRegionCopyRetainRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CrossRegionCopyRetainRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CrossRegionCopyRetainRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CrossRegionCopyRetainRule)
