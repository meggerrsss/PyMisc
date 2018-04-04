s1 = "1x01 Pilot\n1x02 Fastest Man Alive\n1x03 Things You Canxt Outrun\n1x04 Going Rogue\n1x05 Plastique\n1x06 The Flash Is Born\n1x07 Power Outage\n1x08 Flash Vs. Arrow\n1x09 The Man In The Yellow Suit\n1x10 Revenge of The Rogues\n1x11 The Sound and the Fury\n1x12 Crazy For You\n1x13 The Nuclear Man\n1x14 Fallout\n1x15 Out of Time\n1x16 Rogue Time\n1x17 Tricksters\n1x18 All Star Team Up\n1x19 Who Is Harrison Wellsx\n1x20 The Trap\n1x21 Grodd Lives\n1x22 Rogue Air\n1x23 Fast Enough"

s2 = "2x01 The Man Who Saved Central City\n2x02 Flash Of Two Words\n2x03 Family Of Rogues\n2x04 The Fury Of Firestorm\n2x05 The Darkness and The Light\n2x06 Enter Zoom\n2x07 Gorilla Warfare\n2x08 Legends Of Today\n2x09 Running to Stand Still\n2x10 Potential Energy\n2x11 The Reverse Flash Returns\n2x12 Fast Lane\n2x13 Welcome to Earth-2\n2x14 Escape From Earth-2\n2x15 King Shark\n2x16 Trajectory\n2x17 Flash Back\n2x18 Versus Zoom\n2x19 Back To Normal\n2x20 Rupture\n2x21 The Runaway Dinosaur\n2x22 Invincible\n2x23 The Race of His Life"

s3 = "3x01 Flashpoint\n3x02 Paradox\n3x03 Magenta\n3x04 The New Rogues\n3x05 Monster\n3x06 Shade\n3x07 Killer Frost\n3x08 Invasionx\n3x09 The Present\n3x10 Borrowing Problems from the Future\n3x11 Dead or Alive\n3x12 Untouchable\n3x13 Attack on Gorilla City\n3x14 Attack on Central City\n3x15 The Wrath of Savitar\n3x16 Into the Speed Force\n3x17 Duet\n3x18 Abra Kadabra\n3x19 The Once and Future Flash\n3x20 I Know Who You Are\n3x21 Cause and Effect\n3x22 Infantino Street\n3x23 Finish Line"

s1sp = s1.split("\n")
s2sp = s2.split("\n")
s3sp = s1.split("\n")

ns1 = s1sp
ns2 = s2sp
ns3 = s3sp

for i in range(0,len(ns1)):
    ns1[i] = s1sp[i][5:]

for i in range(0,len(ns2)):
    ns2[i] = s2sp[i][5:]

for i in range(0,len(ns3)):
    ns3[i] = s3sp[i][5:]

