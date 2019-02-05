# UFC Pay-Per-View Analysis

Over the past few years, I've become more and more of a fan of mixed martial arts and the UFC. From devestating knockout punches to devestating chokeholds to devestating arm bars, there's just a certain thrill in watching two people beat each other close to death. As one UFC commentator describes the sport, MMA is "high level problem-solving with dire physical consequences".

It's just a curious fact that violence brings folks together. When big fights come around, viewing parties at bars and homes around the world have people tuning in to watch their favourite fighters compete. As a business, the UFC relies on selling Pay-Per-View access to watch their main events. This puts pressure to organize on the company to orchestrate the most exciting fight cards possible - and this excitement is dictated by the talent and charisma of the UFC's fighters.

In this exploratory analysis, my goal is to examine how the UFC's PPV sales have changed over time. Is the UFC selling more PPVs now than in the past? Which fighters bring in the most PPV buys, and how is the UFC promoting events with this in mind? How dependent is the UFC on "superstars" to keep itself growing? I'm going to focus the past 10 years of numbered UFC events (excluding smaller Ultimate Fighter and Fight Night events), dating all the way back to UFC 80 on January 19th, 2008. This dataset was made by scraping information from the infoboxes on each event's Wikipedia page and PPV data from Tapology.com.

<br>
<img src="images\0.png"></img>

Between 2008 and 2010, the median PPV buyrate was hovering closely around 500,000. PPV performance in these years seems pretty consistent, with each year having events that crack more than 1M PPV buys. From 2011 to 2014, the buyrate begins to slide down, culminating in its weakest median ever at 222,500 in 2014. During this period it appears that the UFC's appeal was slowly drifting to low performance (evidenced by the slowly tightening upper whiskers on the box plots); this all changes when the median buyrate skyrockets to its highest ever at 600,000 in 2015.

2015 in my mind marks the beginning of a new era for the UFC, defined by a clear dependance on a small number of superstar fighters (but mainly Conor McGregor). The volatility of this is clearly evident: after a strong 2015 and 2016, the buyrate loses most of its steam save for two massive outliers (the MayMac money fight in 2017 and UFC 229). More on McGregor's impact to come.

<!-- <img src="images\1.png"></img> -->
<img src="images\2.png"></img>

The cumulative PPV Buyrate provides the clearest picture of the UFC's performance over time. In this barplot, each year's bar is the stacked sum of blocks representing all the events that occurred. Events that had PPV buys of at least 1M are labelled and in white; for a height reference, UFC 92 had exactly 1M reported buys.

The UFC's biggest PPV years are best exemplified in 2009, 2010, 2015, and 2016, where the bars are stacked with many tall blocks. 2009 and 2010 also had the added benefit of having a higher number of events, with 15 and 17 in each year respectively. Conversely, weak years like 2014 and 2017 are just small stacks of sliver PPV events. 2018 has so far been a year of extremes, featuring both the worst performing PPV event (UFC 224 at a measly 85,000 buys) as well as the best (UFC 229 with an estimated 2.4 million).

While choosing 1M PPV as a cutoff can seem a little bit arbitrary (many large PPVs come close to this at 800-900+), it does help illustrate an important point. In just the three year span of 2015-2018, the UFC has totalled more 1M+ events (8) than in the seven years prior (7). Only 10% of all events between 2008-2018 have met or surprassed 1M+ buys.

<img src="images\9.png"></img>

The UFC's growing PPV volatility is easily seen by looking at its standard deviaton. While the average PPV buyrate was falling prior to 2015, the standard deviation remained fairly steady around 250,000 buys until 2014. After 2014 both begin to trend upwards - while the average quickly dips back down due to a relatively weak 2017 and 2018 (so far), UFC 229's all-time-high PPV has kept the standard deviation trending up.

The standard deviation is a measure of consistency in the data; ideally, the UFC should want the yearly PPV average to increase while its standard deviation stays low. This would mean consistently high PPV buyrates, and a reliable boatload of cash.

The fact that standard deviation is increasing suggests that the public is mostly interested in tuning in for super fights (e.g. Conor vs. Nate, Conor vs. Khabib). Not an entirely shocking revelation, but it does mean that the UFC needs to keep cultivating superstars to keep their numbers up.

<!-- <img src="images\3.png"></img>
<img src="images\4.png"></img> -->
<img src="images\5.png"></img>

Looking at every PPV event's buyrate plotted over time, the first thing that jumps out to me here is just how much spikey the timeline is. There are only two times in this entire 10 year period where the UFC had two 1M+ events back-to-back: once in 2009 (UFC 93 and UFC 94) and again in late 2015 (UFC 193 and 194). Interestingly, exactly 100 other numbered UFC events happened between these two points. There is no consistent rise in PPV buys; almost every major event is bookended with two mediocre ones in the mid to low 250,000 buy range.

The top ten PPV events of all time are labelled by their title fighters. Two things stand out to me here; first, it seems to be a pretty exclusive club of repeat fighters. Conor McGregor last five fights have all made it to the top ten, and his recent mauling from Khabib Nurmagomedov has blown everything else out of the water as the most successful UFC event of all time. Besides Conor, the three other superstars here are Ronda Rousey, Nate Diaz, and Brock Lesnar, who have all established themselves to be huge event draws at one time or another. The fact that every top 10 event (besides the centennial) has one of these repeat fighters shows the huge financial benefit that these PPV unicorns have for the UFC.

Second, seven of the top ten events all occurred after 2015 and into the present. This recent surge in massive PPV numbers suggests to me that the UFC has been successful in breaking into the mainstream. Beginning with Rousey's reign as the first female superstar and transitioning into McGregor's career as Ireland's trash talking savior, the anticipation for massive fight nights has been palpable up here in Toronto, Canada.

<img src="images\6.png"></img>
<img src="images\7.png"></img>

The barplot ranks all of the headline fighters by an estimate of their PPV buys they've brought in for the UFC (from 2008 to 2018). This estimate was calculated by averaging the PPV buyrates for each fighter based on the events they headlined, and multiplying it by the number of times they fought on cards as headline events. For example, although Eddie Alvarez's average as a headline event is over 1M+ PPV buys (due to facing Conor), he doesn't crack the top 20 in this list because he only headlined that single event.

I think this method provides a decent ranking of each fighter's worth to the UFC. With five of his six headline events surpassing over a million PPV buys, Conor McGregor easily takes the top spot as the UFC's biggest PPV cash cow. His encounters with both Khabib Nurmagomedov and Nate Diaz have propelled the both of them into the top 20, with each earning a wider fanbase seemingly bonded in a fierce dislike of McGregor. 

Georges St-Pierre, Jon Jones, and Anderson Silva, claim the next three spots due to their long, dominant runs as champions in their respective divisions. Following them are Ronda Rousey and Brock Lesnar, two (WWE) superstars who were able to bring in massive audiences with relatively less headline appearances.

It seems to me that the greatest return-on-income for the UFC might come from the fighters on this list who have less appearances, and more potential to evolve into even greater superstars in the future. The fact that fighters like Conor, Ronda, and Lesnar can place so highly with a lower number of fights speaks to the power of superfights to bring in crazy amounts of views. Examples of this in my mind are Khabib and Nate, who have proven themselves to be stone cold killers in their boughts against Conor. The potential return of Brock Lesnar to face Daniel Cormier (or even Jon Jones in a super steroid heavyweight bought) would certainly bring in massive views as well.

I would love to hear from others more informed than me on how accurate these PPV rankings seem, and if there's any way such a method for ranking these fighters could be improved!