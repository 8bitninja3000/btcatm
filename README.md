# DIY-BTC-ATM
#################################################
Not quite working work in progress.
I'm making a Bitcoin atm primarily in python to eventually
be launched as two Raspberry Pi's, one as a server with blockchain credentials,
and one as a client with GUI capabilities.

Please change the server pass, if you value your security.

So it works off of AES encryption and decryption, and keywords at the start.
#################################################

v1.01 -- {

To be absolutely honest idk what I changed but it was super minor

Next once some hardware arrives I'm gonna start adding in that stuff

}
v1.0 -- {

Hey it's actually fully working now.  I had an issue with
updating the gui at one point but I fixed that with some
processevents or something.  That fixed displaying the txid.

Ironed out a few other bugs I can't say I remember all of them.

Notes -- Just ordered some hardware, I'm gonna start working on
that soon.

I guess I should add timeouts so it goes back to the first state.

}

v0.4 -- {

Added/fixed transacting, transacting actually works.

Added framework for implementation of button lights and such.

Notes -- For some reason displaying the txid isn't working.

[We must have some sort of race because only about half of the time does the
price check work.]  FIXED before commit.  Connecting the fxn happened late.

}

v0.3 -- {

Added threading for the occasional price checks.

I better look into issues with fees.  I think I handled it?  Maybe?

Notes - Gotta make state changes a function for lights and stuff still.
Maybe gotta thread.

Then I gotta start interacting with the physical things.

}

v0.2 -- {

Added a bunch of GUI functionality, OUT of stock and such.
The way I do it is a bit sloppy but I guess it's fine.
Just a bit error prone-If a huge spike happens between when a pricecheck happens and a transaction,
it could end up with issues.  But I'm banking on a spike not being big enough to upset the wiggle limits for price.

I added some more stuff but it was like a weed ago so I can't really remember.

Notes - I've gotta make the state changes a function.

Got to make occasional price checks.  Threading?

Also got to interact with physical input and output.
Like buttons and bill validators.

}
v0.1 -- {

Initial upload of what I already had

}
