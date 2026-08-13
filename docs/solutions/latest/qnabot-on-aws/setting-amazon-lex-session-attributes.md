---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/setting-amazon-lex-session-attributes.html
---

# Setting Amazon Lex session attributes
<a name="setting-amazon-lex-session-attributes"></a>

The QnABot on AWS guidance provides support for a question in the content designer UI to set an Amazon Lex session attribute.

In early versions (v5.0.0 and earlier), using Handlebars in an answer would set a session attribute. For example, the following code can set an attribute called `attributeName` to the value `attributeValue`.

```
"{{setSessionAttr 'attributeName' 'attributeValue'}}"
```

Now, you can optionally use a question in the content designer UI to define a set of name/value pairs as session attributes when the answer is returned. There is a field to set a name/value pair, an **Add** button, and a **Delete** button.

The attribute name can be a simple name, such as `myAttribute` or a complex name, such as `myAttribute.subAttribute`. You can also use the *dot* notation to set an attribute several levels deep.

**Note**
Avoid using `appContext` or `qnabotcontext` as attribute names. Setting these might have adverse effects on the system.
