---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/optimize-outbound-calling.html
---

# Optimize your outbound calling reputation
<a name="optimize-outbound-calling"></a>

When making outbound business calls, one of the most difficult tasks is understanding why customers don't answer calls when you dial out. Is the customer deliberately not answering, or are they busy on a work call or answering the door? For businesses it's impossible to know, but you can take action to help increase call success.

The following topics recommend ways to improve your outbound call answer rates.

**Topics**
+ [Step 1: Know your customer's preferred contact method](#know-customer-preferred-contact-method)
+ [Step 2: Brand your calls](#brand-your-calls)
+ [Step 3: Select caller IDs that mean something to your customer](#meaningful-callerid)
+ [Step 4: Make sure your campaign calls valid numbers](#call-valid-numbers)
+ [Step 5: Make outbound calls at optimal times](#optimal-times)
+ [Step 6: Monitor the reputation of your caller IDs](#monitor-reputation)
+ [Step 7: Use multiple numbers as a caller ID](#use-multiple-numbers)
+ [Step 8: Engage with App Vendors](#engage-in-app-vendors)
+ [Step 9: Add messaging to your outreach strategy to let customers know who you are](#add-messaging)
+ [Step 10: Validate your outbound calling strategy](#validate-calling-strategy)

## Step 1: Know your customer's preferred contact method
<a name="know-customer-preferred-contact-method"></a>

One of the biggest mistakes that businesses make is not knowing whether the customer wants to be contacted by telephone call. When the customer engaged with you, did you check whether they want to be reached by phone, e-mail, or text?

Businesses with multi-channel engagement outperform 70% on average compared to business without multi-channel engagement.

## Step 2: Brand your calls
<a name="brand-your-calls"></a>

By using call branding solutions, you can provide enhanced call displays that include your business name, logos, reason for the call, and your service. Branding your calls can increase call answer rates by 30%.

The Amazon Chime SDK and Connect Customer partner with solutions providers such as First Orion and Neustar to offer branded calling services. To discuss the services directly with our partners, visit their websites:
+ [First Orion](https://firstorion.com/amazon-connect-branded-calling-now-available/)
+ [Neustar](https://www.home.neustar)

## Step 3: Select caller IDs that mean something to your customer
<a name="meaningful-callerid"></a>

Not every business is the same. What works for some might not work for others. But there are correlations in how successful outbound campaigns are based on your caller ID. The following suggestions can help you create meaningful caller IDs:
+ **Area localization**. Use a caller ID in the same area as the prospect.
+ **City localization**. Use a caller ID in the same city as the prospect.
+ **Recognizable golden toll free numbers** such as 0800 123 0000.

## Step 4: Make sure your campaign calls valid numbers
<a name="call-valid-numbers"></a>

Many businesses don't have a process for updating customer details. With people more mobile than ever, it's essential for businesses to update contact information. If customers don't answer your calls, we recommend using Amazon Pinpoint to [validate your phone numbers](https://docs.aws.amazon.com/pinpoint/latest/developerguide/validate-phone-numbers.html). The customer may no longer be at the phone number you are calling.

## Step 5: Make outbound calls at optimal times
<a name="optimal-times"></a>

Make sure that calls are placed at the best times. Generally speaking, don't call before 10:00AM or after 5:00PM, as people are at their busiest or need their quiet time. Customers should be called when it's a good for them, depending on their profile. This may mean that you call one customer around noon and another in the afternoon.

In addition, regulations such as TCPA (in the US) and OFCOM (in the UK) provide guidance on when not to call end customers. We strongly recommend that you abide by such regulations.

## Step 6: Monitor the reputation of your caller IDs
<a name="monitor-reputation"></a>

We recommend monitoring the reputation of your caller IDs through a service such as [Free Caller Registry](https://www.freecallerregistry.com/).

Even with the most legitimate outbound call campaigns, if you make enough calls, some people will flag your caller ID as spam. This can manifest in two ways:

1. **Automatic blocking**. Block lists are implemented on a vendor-by-vendor basis. For example, when a certain threshold of reports is reached with application providers such as [Hiya.com](https://www.hiya.com/) on Samsung devices, up to 20% of your prospects will become instantly unreachable.

1. **Complaints**. People can use numerous websites to complain about calls from specific caller IDs. A number of your prospects will search your caller ID online when you call them. If it has a bad reputation, they will be less likely to answer.

The fastest way to recover from a flagged caller ID is to switch to a new phone number. See the next step.

## Step 7: Use multiple numbers as a caller ID
<a name="use-multiple-numbers"></a>

Today, businesses typically embrace an intelligent, more efficient manner of dialing.

For example, one method uses multiple phone numbers when placing outbound calls. Customers are more likely to answer a call if they feel that they are not being called repeatedly by the same number.

## Step 8: Engage with App Vendors
<a name="engage-in-app-vendors"></a>

One of the most difficult issues with the industry as it currently stands is that a large number of vendors provide in-app services to block calls. If one of these in-app services marks your number as spam, you have to pay the premium fees to remove your number from their spam list.

Some of the third party vendors are joining in partnership to increase call answer rates.

## Step 9: Add messaging to your outreach strategy to let customers know who you are
<a name="add-messaging"></a>

When calls go unanswered, you can use SMS to contact prospects. Try the following ideas to increase answer rates.

1. Before calling, send an SMS that tells the customer who you are and when you will call. Optionally, allow the customer to reschedule to a more convenient time.

1. If the prospect doesn't answer, send an SMS to allow them to reschedule the call or request a call back.

1. Use promotional offers or discounts that resonate with your prospects.

## Step 10: Validate your outbound calling strategy
<a name="validate-calling-strategy"></a>

By making data-driven decisions and continuously iterating, you'll have the best chance to deliver real business value. Treat each change to your outbound calling strategy as an experiment, and ensure you can measure and compare the effectiveness of your changes.

One of the best things with Connect Customer is the service is readily available to experiment. You can establish a baseline, then compare any changes to help you to assess how you can succeed.
