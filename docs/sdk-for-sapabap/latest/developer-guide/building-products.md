---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/building-products.html
---

# Building products with SDK
<a name="building-products"></a>

A product or ABAP add-on that consumes AWS services can enhance and extend the capabilities of the SDK. You can build such products to use with the SDK.

**Topics**
+ [Setting a product ID](#product-id)

## Setting a product ID
<a name="product-id"></a>

It is recommended that you set a product ID when establishing a session inside a product or add-on. See the following example for more details.

```
DATA(lo_session) = /aws1/cl_rt_session_aws=>create( 'DEMO' ).
lo_session->set_product_id( 'INVOICE_ANALYZER' ).
```

The product ID must only contain letters, numbers, and underscores with no spaces or special characters. You can match it to the product's technical name or any other identifier. If you develop multiple products or add-ons, the product ID must be unique for each product. For example, the product IDs for Invoice Analyzer, Tax Calculator, and Pricing Engine products can be `INVOICE_ANALYZER`, `TAX_CALCULATOR`, and `PRICING_ENGINE`.

Adding a product ID to the session enhances the telemetry that is sent to AWS with each service call. The product ID and the namespace of the object making the call is included in the telemetry. With this telemetry, Support can identify the product that is making the call in case of your customer facing issues with the SDK. It can help clarify that the call is actually being made by the product, and not your customer's code.
