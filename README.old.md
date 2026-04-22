# Making a GIANT clock

## MVP

We have 500 clocks ticking exactly in time on exactly the same second

## Technical Details

|Category | What is it/Does it do | Description
|-|-|-
[HARDWARE] | MCU  | TI CC1352R chip
[HARDWARE] | RTC  | Alex Chosen Chip
[IMPLEMENTATION] | Radio Sync | 
[OPERATIONALIZATION] | RTC sync  | process at birth to kick off the RTC
[DEVELOPMENT] | PlatformIO | Primary IDE
[DEVELOPMENT] | 
[IMPLEMENTATION] | Secure Boot | Prevents others from stealing our code
[IMPLEMENTATION] | Secure Boot | Prevents others from stealing our code



## What is a CLOCK

It has the time on it,  


Let me tell you the story of this clock. It's super cool. We are using low frequency radio to send out a "follow the leader type pulse" so other clocks birthed from the same factory can remain in lockstep. 

Imagine the windmill fields in NorCal and in the midwest and how they all pulse in time at night. This is done and accomplished because they have a clear view of the sky and are able to use the GPS clock for syncing.  unfortunately, we don't have GPS internally at conferences and GPS does not work in crowded areas for synchronizing clocks just because of the latency you're not gonna get millisecond accuracy across thousands advices. You're gonna get millisecond accuracy across hundreds of devices. So what we're trying to do is create a clock that when birth from the factory has a set RTC on it, and that RTC will continue to tick time and it will drift up to three seconds in a year, or based off of the crystal that we use an RTC that we choose and how we set up the system to set it initially. 

To accommodate for the drift pattern of the clock, we are going to utilize a low frequency radio spectrum where we will have authenticated clocks that use an HVAC or some other method of public key signature verification to validate an authoritative source of time. 

So we have a clock. It ticks in time. So we have 10 clocks, and we want to make them tick in time. Passively. And all this project needs to do, is keep accurate time down to the MS in a crowd, with a secondary feature of setting a localized light show out of a list of 255 that are available. 


So the UX looks like this: 

This was inspired by Smarter Every Day and Destin's videos on fireflies. We get the clock, and we get it ticking in time, and we get an LED that fades up and down in time with all the other clocks. 

I get a "firefly". It is ALDREADY programmed, and it blinks every imnute in time with other fireflies. It takes its current tick count out of the air from an authoritive source of time (or another firefly that has promoted itself to leader after enough time has passed when one wasn't around, if a leader comes back into range snap to the leader). The device is 2cmx2cm with its own backup battery for the RTC, and THE MOST IMPORTANT PART IS THIS IS A FUCKING CLOCK. It does not do ANYTHING fancy. The fanciest thing it does, is tell the board it's connected to over i2c what the current unix time is and what the current localized light show slot is. This light-show slot is meant to be used by the parent board it is attached to. 

In effect this will enable not only a synchronized light fade across multiple disconnected IoT mother-boards, but if tuned accurately enough we may be able to synchronize duty cycles on PWM. 

The reason we are fading up is because the duty-cycle synced PWM is a WAG: Wildly Ambitious Goal. It will be the target of maybe version 4 or 5 of this device. Not out the gate, that would require a POT onboard for tuning, or an AutoPOT