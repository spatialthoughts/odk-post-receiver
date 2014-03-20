ODK POST Receiver
=================

A simple appengine server that receives and displays JSON POST requests from ODK (OpenDataKit) Aggregate.

How to use
==========

If you are a running ODK Aggregate server, you can use this server to test the Z-Alpha JSON publisher.

Select 'Publish' next to any form and select Z-Alpha JSON publisher. Specify *http://odk-post-receiver.appspot.com* as the Server URL and leave the Authorization Token field empty.

![Screenshot of Z-Alpha JSON Publisher](http://imgur.com/4q2jcbK.png)

Once configured, the ODK Aggregate server will stream new form submissions as JSON POST requests to this server. If the ODK Aggregate server was configured correctly, you will see your form submissions listed at http://odk-post-receiver.appspot.com

**Note: All data will be automacally purged from the server within 1 hour.**

LICENSE
=======
Copyright 2014 Ujaval Gandhi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
