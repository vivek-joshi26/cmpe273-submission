You will be implementing a clone of Bitly REST API using Python Flask (Links to an external site.) framework.
Data persistence is not required for your implementation. Your cloned version of Bitly must have these APIs:

1. Shorten a link (https://dev.bitly.com/api-reference#createBitlink)
   Method-
   1. POST -  /v4/shorten
   Test from cmd-
   curl -H 'Content-Type: application/json' -X POST \
   -d '{
  "long_url": "https://dev.bitly.com",
  "domain": "bit.ly",
  "group_guid": "Ba1bc23dE4F"
}' \
http://localhost:8070/v4/shorten

2. Create a Bitlink (https://dev.bitly.com/api-reference#createFullBitlink)
    Method-
   1. Post -  /v4/bitlinks

3. Update a Bitlink (https://dev.bitly.com/api-reference#updateBitlink)
    Method-
   1. PATCH -  /v4/bitlinks/{bitlink}

4. Retrieve a Bitlink (https://dev.bitly.com/api-reference#getBitlink)
    Method-
   1. GET -   /v4/bitlinks/{bitlink}

5. Get Clicks for a Bitlink (https://dev.bitly.com/api-reference#getClicksForBitlink)
    Method-
   1. GET -    /v4/bitlinks/{bitlink}/clicks