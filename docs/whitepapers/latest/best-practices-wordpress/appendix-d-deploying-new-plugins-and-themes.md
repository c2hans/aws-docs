---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/appendix-d-deploying-new-plugins-and-themes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix D: Deploying new plugins and themes
<a name="appendix-d-deploying-new-plugins-and-themes"></a>

 Few websites remain static. In most cases, you will periodically add publicly available WordPress themes and plugins or upgrade to a newer WordPress version. In other cases, you will develop your own custom themes and plugins from scratch.

 Any time you are making a structural change to your WordPress installation there is a certain risk of introducing unforeseen problems. At the very least, take a backup of your application code, configuration, and database before applying any significant change (such as installing a new plugin). For websites of business or other value, test those changes in a separate staging environment first. With AWS, it is easy to replicate the configuration of your production environment and run the whole deployment process in a safe manner. After you are done with your tests, you can simply tear down your test environment and stop paying for those resources. Later, this whitepaper discusses some WordPress-specific considerations.

 Some plugins write configuration information to the `wp_options` database table (or introduce database schema changes), whereas others create configuration files in the WordPress installation directory. Because we have moved the database and storage to shared platforms, these changes are immediately available to all of your running instances without any further effort on your part.

 When deploying new themes in WordPress, a little more effort may be required. If you are only making use of Amazon EFS to store all your WordPress installation files, then new themes will be immediately available to all running instances. However, if you are offloading static content to Amazon S3, you must process a copy of these to the right bucket location. Plugins like W3 Total Cache provide a way for you to manually initiate that task. Alternatively, you could automate this step as part of a build process.

 Because theme assets can be cached on CloudFront and at the browser, you need a way to invalidate older versions when you deploy changes. The best way to achieve this is by including some sort of version identifier in your object. This identifier can be a query string with a date-time stamp or a random string. If you use the W3 Total Cache plugin, you can update a media query string that is appended to the URLs of media files.
