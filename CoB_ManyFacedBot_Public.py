import praw
import os
import re
import Battle
import Duel
import Joust
import Boxing
import time
import Army
import random
import Globals

reddit = praw.Reddit(user_agent=os.environ['AGENT_NAME'] ,
                     client_id=os.environ['PRAW_ID'] ,
                     client_secret=os.environ['PRAW_SECRET'] ,
                     password=os.environ['REDDIT_PW'] ,
                     username=os.environ['REDDIT_USER']
)

print ("---\n")
Globals.Globals()

def traits(): #Get an input here eventually which determines whether to do random rolls or just good/bad/neutral
    
    roll = random.randint(1,638)
    if(roll==1):
        outcome = "Accessible"
    elif(roll==2):
        outcome = "Active"
    elif(roll==3):
        outcome = "Adaptable"
    elif(roll==4):
        outcome = "Admirable"
    elif(roll==5):
        outcome = "Adventurous"
    elif(roll==6):
        outcome = "Agreeable"
    elif(roll==7):
        outcome = "Alert"
    elif(roll==8):
        outcome = "Allocentric"
    elif(roll==9):
        outcome = "Amiable"
    elif(roll==10):
        outcome = "Anticipative"
    elif(roll==11):
        outcome = "Appreciative"
    elif(roll==12):
        outcome = "Articulate"
    elif(roll==13):
        outcome = "Aspiring"
    elif(roll==14):
        outcome = "Athletic"
    elif(roll==15):
        outcome = "Attractive"
    elif(roll==16):
        outcome = "Balanced"
    elif(roll==17):
        outcome = "Benevolent"
    elif(roll==18):
        outcome = "Brilliant"
    elif(roll==19):
        outcome = "Calm"
    elif(roll==20):
        outcome = "Capable"
    elif(roll==21):
        outcome = "Captivating"
    elif(roll==22):
        outcome = "Caring"
    elif(roll==23):
        outcome = "Challenging"
    elif(roll==24):
        outcome = "Charismatic"
    elif(roll==25):
        outcome = "Charming"
    elif(roll==26):
        outcome = "Cheerful"
    elif(roll==27):
        outcome = "Clean"
    elif(roll==28):
        outcome = "Clear-headed"
    elif(roll==29):
        outcome = "Clever"
    elif(roll==30):
        outcome = "Colorful"
    elif(roll==31):
        outcome = "Companionly"
    elif(roll==32):
        outcome = "Compassionate"
    elif(roll==33):
        outcome = "Conciliatory"
    elif(roll==34):
        outcome = "Confident"
    elif(roll==35):
        outcome = "Conscientious"
    elif(roll==36):
        outcome = "Considerate"
    elif(roll==37):
        outcome = "Constant"
    elif(roll==38):
        outcome = "Contemplative"
    elif(roll==39):
        outcome = "Cooperative"
    elif(roll==40):
        outcome = "Courageous"
    elif(roll==41):
        outcome = "Courteous"
    elif(roll==42):
        outcome = "Creative"
    elif(roll==43):
        outcome = "Cultured"
    elif(roll==44):
        outcome = "Curious"
    elif(roll==45):
        outcome = "Daring"
    elif(roll==46):
        outcome = "Debonair"
    elif(roll==47):
        outcome = "Decent"
    elif(roll==48):
        outcome = "Decisive"
    elif(roll==49):
        outcome = "Dedicated"
    elif(roll==50):
        outcome = "Deep"
    elif(roll==51):
        outcome = "Dignified"
    elif(roll==52):
        outcome = "Directed"
    elif(roll==53):
        outcome = "Disciplined"
    elif(roll==54):
        outcome = "Discreet"
    elif(roll==55):
        outcome = "Dramatic"
    elif(roll==56):
        outcome = "Dutiful"
    elif(roll==57):
        outcome = "Dynamic"
    elif(roll==58):
        outcome = "Earnest"
    elif(roll==59):
        outcome = "Ebullient"
    elif(roll==60):
        outcome = "Educated"
    elif(roll==61):
        outcome = "Efficient"
    elif(roll==62):
        outcome = "Elegant"
    elif(roll==63):
        outcome = "Eloquent"
    elif(roll==64):
        outcome = "Empathetic"
    elif(roll==65):
        outcome = "Energetic"
    elif(roll==66):
        outcome = "Enthusiastic"
    elif(roll==67):
        outcome = "Esthetic"
    elif(roll==68):
        outcome = "Exciting"
    elif(roll==69):
        outcome = "Extraordinary"
    elif(roll==70):
        outcome = "Fair"
    elif(roll==71):
        outcome = "Faithful"
    elif(roll==72):
        outcome = "Farsighted"
    elif(roll==73):
        outcome = "Felicific"
    elif(roll==74):
        outcome = "Firm"
    elif(roll==75):
        outcome = "Flexible"
    elif(roll==76):
        outcome = "Focused"
    elif(roll==77):
        outcome = "Forceful"
    elif(roll==78):
        outcome = "Forgiving"
    elif(roll==79):
        outcome = "Forthright"
    elif(roll==80):
        outcome = "Freethinking"
    elif(roll==81):
        outcome = "Friendly"
    elif(roll==82):
        outcome = "Fun-loving"
    elif(roll==83):
        outcome = "Gallant"
    elif(roll==84):
        outcome = "Generous"
    elif(roll==85):
        outcome = "Gentle"
    elif(roll==86):
        outcome = "Genuine"
    elif(roll==87):
        outcome = "Good-natured"
    elif(roll==88):
        outcome = "Gracious"
    elif(roll==89):
        outcome = "Hardworking"
    elif(roll==90):
        outcome = "Healthy"
    elif(roll==91):
        outcome = "Hearty"
    elif(roll==92):
        outcome = "Helpful"
    elif(roll==93):
        outcome = "Heroic"
    elif(roll==94):
        outcome = "High-minded"
    elif(roll==95):
        outcome = "Honest"
    elif(roll==96):
        outcome = "Honorable"
    elif(roll==97):
        outcome = "Humble"
    elif(roll==98):
        outcome = "Humorous"
    elif(roll==99):
        outcome = "Idealistic"
    elif(roll==100):
        outcome = "Imaginatives"
        
    elif(roll==101):
        outcome = "Impressive"
    elif(roll==102):
        outcome = "Incisive"
    elif(roll==103):
        outcome = "Incorruptible"
    elif(roll==104):
        outcome = "Independent"
    elif(roll==105):
        outcome = "Individualistic"
    elif(roll==106):
        outcome = "Innovative"
    elif(roll==107):
        outcome = "Inoffensive"
    elif(roll==108):
        outcome = "Insightful"
    elif(roll==109):
        outcome = "Insouciant"
    elif(roll==110):
        outcome = "Intelligent"
    elif(roll==111):
        outcome = "Intuitive"
    elif(roll==112):
        outcome = "Invulnerable"
    elif(roll==113):
        outcome = "Kind"
    elif(roll==114):
        outcome = "Knowledgeable"
    elif(roll==115):
        outcome = "Leaderly"
    elif(roll==116):
        outcome = "Leisurely"
    elif(roll==117):
        outcome = "Liberal"
    elif(roll==118):
        outcome = "Logical"
    elif(roll==119):
        outcome = "Lovable"
    elif(roll==120):
        outcome = "Loyal"
    elif(roll==121):
        outcome = "Lyrical"
    elif(roll==122):
        outcome = "Magnanimous"
    elif(roll==123):
        outcome = "Many-sided"
    elif(roll==124):
        outcome = "Masculine"
    elif(roll==125):
        outcome = "Mature"
    elif(roll==126):
        outcome = "Methodical"
    elif(roll==127):
        outcome = "Maticulous"
    elif(roll==128):
        outcome = "Moderate"
    elif(roll==129):
        outcome = "Modest"
    elif(roll==130):
        outcome = "Multi-leveled"
    elif(roll==131):
        outcome = "Neat"
    elif(roll==132):
        outcome = "Nonauthoritarian"
    elif(roll==133):
        outcome = "Objective"
    elif(roll==134):
        outcome = "Observant"
    elif(roll==135):
        outcome = "Open"
    elif(roll==136):
        outcome = "Optimistic"
    elif(roll==137):
        outcome = "Orderly"
    elif(roll==138):
        outcome = "Organized"
    elif(roll==139):
        outcome = "Original"
    elif(roll==140):
        outcome = "Painstaking"
    elif(roll==141):
        outcome = "Passionate"
    elif(roll==142):
        outcome = "Patient"
    elif(roll==143):
        outcome = "Patriotic"
    elif(roll==144):
        outcome = "Peaceful"
    elif(roll==145):
        outcome = "Perceptive"
    elif(roll==146):
        outcome = "Perfectionist"
    elif(roll==147):
        outcome = "Personable"
    elif(roll==148):
        outcome = "Persuasive"
    elif(roll==149):
        outcome = "Planful"
    elif(roll==150):
        outcome = "Playful"
    elif(roll==151):
        outcome = "Polished"
    elif(roll==152):
        outcome = "Popular"
    elif(roll==153):
        outcome = "Practical"
    elif(roll==154):
        outcome = "Precise"
    elif(roll==155):
        outcome = "Principled"
    elif(roll==156):
        outcome = "Profound"
    elif(roll==157):
        outcome = "Protean"
    elif(roll==158):
        outcome = "Protective"
    elif(roll==159):
        outcome = "Providential"
    elif(roll==160):
        outcome = "Prudent"
    elif(roll==161):
        outcome = "Punctual"
    elif(roll==162):
        outcome = "Pruposeful"
    elif(roll==163):
        outcome = "Rational"
    elif(roll==164):
        outcome = "Realistic"
    elif(roll==165):
        outcome = "Reflective"
    elif(roll==166):
        outcome = "Relaxed"
    elif(roll==167):
        outcome = "Reliable"
    elif(roll==168):
        outcome = "Resourceful"
    elif(roll==169):
        outcome = "Respectful"
    elif(roll==170):
        outcome = "Responsible"
    elif(roll==171):
        outcome = "Responsive"
    elif(roll==172):
        outcome = "Reverential"
    elif(roll==173):
        outcome = "Romantic"
    elif(roll==174):
        outcome = "Rustic"
    elif(roll==175):
        outcome = "Sage"
    elif(roll==176):
        outcome = "Sane"
    elif(roll==177):
        outcome = "Scholarly"
    elif(roll==178):
        outcome = "Scrupulous"
    elif(roll==179):
        outcome = "Secure"
    elif(roll==180):
        outcome = "Selfless"
    elif(roll==181):
        outcome = "Self-critical"
    elif(roll==182):
        outcome = "Self-defacing"
    elif(roll==183):
        outcome = "Self-denying"
    elif(roll==184):
        outcome = "Self-reliant"
    elif(roll==185):
        outcome = "Self-sufficent"
    elif(roll==186):
        outcome = "Sensitive"
    elif(roll==187):
        outcome = "Sentimental"
    elif(roll==188):
        outcome = "Seraphic"
    elif(roll==189):
        outcome = "Serious"
    elif(roll==190):
        outcome = "Sexy"
    elif(roll==191):
        outcome = "Sharing"
    elif(roll==192):
        outcome = "Shrewd"
    elif(roll==193):
        outcome = "Simple"
    elif(roll==194):
        outcome = "Skillful"
    elif(roll==195):
        outcome = "Sober"
    elif(roll==196):
        outcome = "Sociable"
    elif(roll==197):
        outcome = "Solid"
    elif(roll==198):
        outcome = "Sophisticated"
    elif(roll==199):
        outcome = "Spontaneous"
    elif(roll==200):
        outcome = "Sporting"
        
    elif(roll==201):
        outcome = "Stable"
    elif(roll==202):
        outcome = "Steadfast"
    elif(roll==203):
        outcome = "Steady"
    elif(roll==204):
        outcome = "Stoic"
    elif(roll==205):
        outcome = "Strong"
    elif(roll==206):
        outcome = "Studious"
    elif(roll==207):
        outcome = "Suave"
    elif(roll==208):
        outcome = "Subtle"
    elif(roll==209):
        outcome = "Sweet"
    elif(roll==210):
        outcome = "Sympathetic"
    elif(roll==211):
        outcome = "Systematic"
    elif(roll==212):
        outcome = "Tasteful"
    elif(roll==213):
        outcome = "Teacherly"
    elif(roll==214):
        outcome = "Thorough"
    elif(roll==215):
        outcome = "Tidy"
    elif(roll==216):
        outcome = "Tolerant"
    elif(roll==217):
        outcome = "Tractable"
    elif(roll==218):
        outcome = "Trusting"
    elif(roll==219):
        outcome = "Uncomplaining"
    elif(roll==220):
        outcome = "Understanding"
    elif(roll==221):
        outcome = "Undogmatic"
    elif(roll==222):
        outcome = "Unfoolable"
    elif(roll==223):
        outcome = "Uptight"
    elif(roll==224):
        outcome = "Urbane"
    elif(roll==225):
        outcome = "Venturesome"
    elif(roll==226):
        outcome = "Vivacious"
    elif(roll==227):
        outcome = "Warm"
    elif(roll==228):
        outcome = "Well-bred"
    elif(roll==229):
        outcome = "Well-read"
    elif(roll==230):
        outcome = "Well-rounded"
    elif(roll==231):
        outcome = "Winning"
    elif(roll==232):
        outcome = "Wise"
    elif(roll==233):
        outcome = "Witty"
    elif(roll==234):
        outcome = "Youthful"

        
    elif(roll==235):
        outcome = "Absentminded"
    elif(roll==236):
        outcome = "Aggressive"
    elif(roll==237):
        outcome = "Ambitious"
    elif(roll==238):
        outcome = "Amusing"
    elif(roll==239):
        outcome = "Artful"
    elif(roll==240):
        outcome = "Ascetic"
    elif(roll==241):
        outcome = "Authoritarian"
    elif(roll==242):
        outcome = "Big-thinking"
    elif(roll==243):
        outcome = "Boyish"
    elif(roll==244):
        outcome = "Breezy"
    elif(roll==245):
        outcome = "Businesslike"
    elif(roll==246):
        outcome = "Busy"
    elif(roll==247):
        outcome = "Casual"
    elif(roll==248):
        outcome = "Crebral"
    elif(roll==249):
        outcome = "Chummy"
    elif(roll==250):
        outcome = "Circumspect"
    elif(roll==251):
        outcome = "Competitive"
    elif(roll==252):
        outcome = "Complex"
    elif(roll==253):
        outcome = "Confidential"
    elif(roll==254):
        outcome = "Conservative"
    elif(roll==255):
        outcome = "Contradictory"
    elif(roll==256):
        outcome = "Crisp"
    elif(roll==257):
        outcome = "Cute"
    elif(roll==258):
        outcome = "Deceptive"
    elif(roll==259):
        outcome = "Determined"
    elif(roll==260):
        outcome = "Dominating"
    elif(roll==261):
        outcome = "Dreamy"
    elif(roll==262):
        outcome = "Driving"
    elif(roll==263):
        outcome = "Droll"
    elif(roll==264):
        outcome = "Dry"
    elif(roll==265):
        outcome = "Earthy"
    elif(roll==266):
        outcome = "Effeminate"
    elif(roll==267):
        outcome = "Emotional"
    elif(roll==268):
        outcome = "Enigmatic"
    elif(roll==269):
        outcome = "Experimental"
    elif(roll==270):
        outcome = "Familial"
    elif(roll==271):
        outcome = "Folksy"
    elif(roll==272):
        outcome = "Formal"
    elif(roll==273):
        outcome = "Freewheeling"
    elif(roll==274):
        outcome = "Frugal"
    elif(roll==275):
        outcome = "Glamorous"
    elif(roll==276):
        outcome = "Guileless"
    elif(roll==277):
        outcome = "High-spirited"
    elif(roll==278):
        outcome = "Huried"
    elif(roll==279):
        outcome = "Hypnotic"
    elif(roll==280):
        outcome = "Iconoclastic"
    elif(roll==281):
        outcome = "Idiosyncratic"
    elif(roll==282):
        outcome = "Impassive"
    elif(roll==283):
        outcome = "Impersonal"
    elif(roll==284):
        outcome = "Impressionable"
    elif(roll==285):
        outcome = "Intense"
    elif(roll==286):
        outcome = "Invisible"
    elif(roll==287):
        outcome = "Irreligious"
    elif(roll==288):
        outcome = "Irreverent"
    elif(roll==289):
        outcome = "Maternal"
    elif(roll==290):
        outcome = "Mellow"
    elif(roll==291):
        outcome = "Modern"
    elif(roll==292):
        outcome = "Moralistic"
    elif(roll==293):
        outcome = "Mystical"
    elif(roll==294):
        outcome = "Neutral"
    elif(roll==295):
        outcome = "Noncommittal"
    elif(roll==296):
        outcome = "Noncompetitive"
    elif(roll==297):
        outcome = "Obedient"
    elif(roll==298):
        outcome = "Old-fashined"
    elif(roll==299):
        outcome = "Ordinary"
    elif(roll==300):
        outcome = "Outspoken"
        
    elif(roll==301):
        outcome = "Paternalistic"
    elif(roll==302):
        outcome = "Physical"
    elif(roll==303):
        outcome = "Placid"
    elif(roll==304):
        outcome = "Political"
    elif(roll==305):
        outcome = "Predictable"
    elif(roll==306):
        outcome = "Preoccupied"
    elif(roll==307):
        outcome = "Private"
    elif(roll==308):
        outcome = "Progressive"
    elif(roll==309):
        outcome = "Proud"
    elif(roll==310):
        outcome = "Pure"
    elif(roll==311):
        outcome = "Questioning"
    elif(roll==312):
        outcome = "Quiet"
    elif(roll==313):
        outcome = "Religious"
    elif(roll==314):
        outcome = "Reserved"
    elif(roll==315):
        outcome = "Restrained"
    elif(roll==316):
        outcome = "Retiring"
    elif(roll==317):
        outcome = "Sarcastic"
    elif(roll==318):
        outcome = "Self-conscious"
    elif(roll==319):
        outcome = "Sensual"
    elif(roll==320):
        outcome = "Skeptical"
    elif(roll==321):
        outcome = "Smooth"
    elif(roll==322):
        outcome = "Soft"
    elif(roll==323):
        outcome = "Solemn"
    elif(roll==324):
        outcome = "Solitary"
    elif(roll==325):
        outcome = "Stern"
    elif(roll==326):
        outcome = "Stolid"
    elif(roll==327):
        outcome = "Strict"
    elif(roll==328):
        outcome = "Stubborn"
    elif(roll==329):
        outcome = "Stylish"
    elif(roll==330):
        outcome = "Subjective"
    elif(roll==331):
        outcome = "Surprising"
    elif(roll==332):
        outcome = "Soft"
    elif(roll==333):
        outcome = "Tough"
    elif(roll==334):
        outcome = "Unaggressive"
    elif(roll==335):
        outcome = "Unambitious"
    elif(roll==336):
        outcome = "Unceremonious"
    elif(roll==337):
        outcome = "Unchanging"
    elif(roll==338):
        outcome = "Undemanding"
    elif(roll==339):
        outcome = "Unfathomable"
    elif(roll==340):
        outcome = "Unhurried"
    elif(roll==341):
        outcome = "Uninhibited"
    elif(roll==342):
        outcome = "Unpatriotic"
    elif(roll==343):
        outcome = "Unpredicatable"
    elif(roll==344):
        outcome = "Unreligious"
    elif(roll==345):
        outcome = "Unsentimental"
    elif(roll==346):
        outcome = "Whimsical"

        
    elif(roll==347):
        outcome = "Abrasive"
    elif(roll==348):
        outcome = "Abrupt"
    elif(roll==349):
        outcome = "Agonizing"
    elif(roll==350):
        outcome = "Aimless"
    elif(roll==351):
        outcome = "Airy"
    elif(roll==352):
        outcome = "Aloof"
    elif(roll==353):
        outcome = "Amoral"
    elif(roll==354):
        outcome = "Angry"
    elif(roll==355):
        outcome = "Anxious"
    elif(roll==356):
        outcome = "Apathetic"
    elif(roll==357):
        outcome = "Arbitrary"
    elif(roll==358):
        outcome = "Argumentative"
    elif(roll==359):
        outcome = "Arrogantt"
    elif(roll==360):
        outcome = "Artificial"
    elif(roll==361):
        outcome = "Asocial"
    elif(roll==362):
        outcome = "Assertive"
    elif(roll==363):
        outcome = "Astigmatice"
    elif(roll==364):
        outcome = "Barbaric"
    elif(roll==365):
        outcome = "Bewildered"
    elif(roll==366):
        outcome = "Bizarre"
    elif(roll==367):
        outcome = "Bland"
    elif(roll==368):
        outcome = "Blunt"
    elif(roll==369):
        outcome = "Boisterous"
    elif(roll==370):
        outcome = "Brittle"
    elif(roll==371):
        outcome = "Brutal"
    elif(roll==372):
        outcome = "Calculating"
    elif(roll==373):
        outcome = "Callous"
    elif(roll==374):
        outcome = "Cantakerous"
    elif(roll==375):
        outcome = "Careless"
    elif(roll==376):
        outcome = "Cautious"
    elif(roll==377):
        outcome = "Charmless"
    elif(roll==378):
        outcome = "Childish"
    elif(roll==379):
        outcome = "Clumsy"
    elif(roll==380):
        outcome = "Coarse"
    elif(roll==381):
        outcome = "Cold"
    elif(roll==382):
        outcome = "Colorless"
    elif(roll==383):
        outcome = "Complacent"
    elif(roll==384):
        outcome = "Complaintive"
    elif(roll==385):
        outcome = "Compulsive"
    elif(roll==386):
        outcome = "Conceited"
    elif(roll==387):
        outcome = "Condemnatory"
    elif(roll==388):
        outcome = "Conformist"
    elif(roll==389):
        outcome = "Confused"
    elif(roll==390):
        outcome = "Contemptible"
    elif(roll==391):
        outcome = "Conventional"
    elif(roll==392):
        outcome = "Cowardly"
    elif(roll==393):
        outcome = "Crafty"
    elif(roll==394):
        outcome = "Crass"
    elif(roll==395):
        outcome = "Crazy"
    elif(roll==396):
        outcome = "Criminal"
    elif(roll==397):
        outcome = "Critical"
    elif(roll==398):
        outcome = "Crude"
    elif(roll==399):
        outcome = "Cruel"
    elif(roll==400):
        outcome = "Cynical"
        
    elif(roll==401):
        outcome = "Decadent"
    elif(roll==402):
        outcome = "Deceitful"
    elif(roll==403):
        outcome = "Delicate"
    elif(roll==404):
        outcome = "Demanding"
    elif(roll==405):
        outcome = "Dependent"
    elif(roll==406):
        outcome = "Desperate"
    elif(roll==407):
        outcome = "Destructive"
    elif(roll==408):
        outcome = "Devious"
    elif(roll==409):
        outcome = "Difficult"
    elif(roll==410):
        outcome = "Dirty"
    elif(roll==411):
        outcome = "Disconcerting"
    elif(roll==412):
        outcome = "Discontented"
    elif(roll==413):
        outcome = "Discouraging"
    elif(roll==414):
        outcome = "Discourteous"
    elif(roll==415):
        outcome = "Dishonest"
    elif(roll==416):
        outcome = "Disloyal"
    elif(roll==417):
        outcome = "Disobedient"
    elif(roll==418):
        outcome = "Disorderly"
    elif(roll==419):
        outcome = "Disorganized"
    elif(roll==420):
        outcome = "Disputatious"
    elif(roll==421):
        outcome = "Disrespectful"
    elif(roll==422):
        outcome = "Disruptive"
    elif(roll==423):
        outcome = "Dissolute"
    elif(roll==424):
        outcome = "Dissonant"
    elif(roll==425):
        outcome = "Distractible"
    elif(roll==426):
        outcome = "Disturbing"
    elif(roll==427):
        outcome = "Dogmatic"
    elif(roll==428):
        outcome = "Domineering"
    elif(roll==429):
        outcome = "Dull"
    elif(roll==430):
        outcome = "Discouraged"
    elif(roll==431):
        outcome = "Egocentric"
    elif(roll==432):
        outcome = "Enervated"
    elif(roll==433):
        outcome = "Envious"
    elif(roll==434):
        outcome = "Erratic"
    elif(roll==435):
        outcome = "Escapist"
    elif(roll==436):
        outcome = "Excitable"
    elif(roll==437):
        outcome = "Expedient"
    elif(roll==438):
        outcome = "Extravagant"
    elif(roll==439):
        outcome = "Extreme"
    elif(roll==440):
        outcome = "Faithless"
    elif(roll==441):
        outcome = "False"
    elif(roll==442):
        outcome = "Fanatical"
    elif(roll==443):
        outcome = "Fanciful"
    elif(roll==444):
        outcome = "Fatalistic"
    elif(roll==445):
        outcome = "Fawning"
    elif(roll==446):
        outcome = "Fearful"
    elif(roll==447):
        outcome = "Fickle"
    elif(roll==448):
        outcome = "Fiery"
    elif(roll==449):
        outcome = "Fixed"
    elif(roll==450):
        outcome = "Flamboyant"
    elif(roll==451):
        outcome = "Foolish"
    elif(roll==452):
        outcome = "Forgetful"
    elif(roll==453):
        outcome = "Fraudulent"
    elif(roll==454):
        outcome = "Frightening"
    elif(roll==455):
        outcome = "Frivolous"
    elif(roll==456):
        outcome = "Gloomy"
    elif(roll==457):
        outcome = "Graceless"
    elif(roll==458):
        outcome = "Grand"
    elif(roll==459):
        outcome = "Greedy"
    elif(roll==460):
        outcome = "Grim"
    elif(roll==461):
        outcome = "Gullible"
    elif(roll==462):
        outcome = "Hateful"
    elif(roll==463):
        outcome = "Haughty"
    elif(roll==464):
        outcome = "Hedonistic"
    elif(roll==465):
        outcome = "Hesitant"
    elif(roll==466):
        outcome = "Hidebound"
    elif(roll==467):
        outcome = "High-handed"
    elif(roll==468):
        outcome = "Hostile"
    elif(roll==469):
        outcome = "Ignorant"
    elif(roll==470):
        outcome = "Imitative"
    elif(roll==471):
        outcome = "Impatient"
    elif(roll==472):
        outcome = "Impractical"
    elif(roll==473):
        outcome = "Imprudent"
    elif(roll==474):
        outcome = "Impulsive"
    elif(roll==475):
        outcome = "Inconsiderate"
    elif(roll==476):
        outcome = "Incurious"
    elif(roll==477):
        outcome = "Indecisive"
    elif(roll==478):
        outcome = "Indulgent"
    elif(roll==479):
        outcome = "Inert"
    elif(roll==480):
        outcome = "Inhibited"
    elif(roll==481):
        outcome = "Insecure"
    elif(roll==482):
        outcome = "Insensitive"
    elif(roll==483):
        outcome = "Insincere"
    elif(roll==484):
        outcome = "Insultinge"
    elif(roll==485):
        outcome = "Intolerant"
    elif(roll==486):
        outcome = "Irascible"
    elif(roll==487):
        outcome = "Irrational"
    elif(roll==488):
        outcome = "Irresponsible"
    elif(roll==489):
        outcome = "Irritable"
    elif(roll==490):
        outcome = "Lazy"
    elif(roll==491):
        outcome = "Libidinous"
    elif(roll==492):
        outcome = "Loquacious"
    elif(roll==493):
        outcome = "Malicious"
    elif(roll==494):
        outcome = "Mannered"
    elif(roll==495):
        outcome = "Mannerless"
    elif(roll==496):
        outcome = "Mawkish"
    elif(roll==497):
        outcome = "Mealy-mouthed"
    elif(roll==498):
        outcome = "Mechanical"
    elif(roll==499):
        outcome = "Meddlesome"
    elif(roll==500):
        outcome = "Melancholice"
        
    elif(roll==501):
        outcome = "Meretricious"
    elif(roll==502):
        outcome = "Messy"
    elif(roll==503):
        outcome = "Miserable"
    elif(roll==504):
        outcome = "Miserly"
    elif(roll==505):
        outcome = "Misguided"
    elif(roll==506):
        outcome = "Mistaken"
    elif(roll==507):
        outcome = "Money-minded"
    elif(roll==508):
        outcome = "Monstrous"
    elif(roll==509):
        outcome = "Moody"
    elif(roll==510):
        outcome = "Morbid"
    elif(roll==511):
        outcome = "Muddle-headed"
    elif(roll==512):
        outcome = "Naive"
    elif(roll==513):
        outcome = "Narcissistic"
    elif(roll==514):
        outcome = "Narrow"
    elif(roll==515):
        outcome = "Narrow-minded"
    elif(roll==516):
        outcome = "Natty"
    elif(roll==517):
        outcome = "Negativistic"
    elif(roll==518):
        outcome = "Neglectful"
    elif(roll==519):
        outcome = "Neurotic"
    elif(roll==520):
        outcome = "Nihilistic"
    elif(roll==521):
        outcome = "Obnoxious"
    elif(roll==522):
        outcome = "Obsessive"
    elif(roll==523):
        outcome = "Obvious"
    elif(roll==524):
        outcome = "Odd"
    elif(roll==525):
        outcome = "Offhand"
    elif(roll==526):
        outcome = "One-dimensional"
    elif(roll==527):
        outcome = "One-sided"
    elif(roll==528):
        outcome = "Opinionated"
    elif(roll==529):
        outcome = "Opportunistic"
    elif(roll==530):
        outcome = "Oppressed"
    elif(roll==531):
        outcome = "Outrageous"
    elif(roll==532):
        outcome = "Overimaginative"
    elif(roll==533):
        outcome = "Paranoid"
    elif(roll==534):
        outcome = "Passive"
    elif(roll==535):
        outcome = "Pedantic"
    elif(roll==536):
        outcome = "Perverse"
    elif(roll==537):
        outcome = "Petty"
    elif(roll==538):
        outcome = "Pharisaical"
    elif(roll==539):
        outcome = "Phlegmatic"
    elif(roll==540):
        outcome = "Ploddingle"
    elif(roll==541):
        outcome = "Pompous"
    elif(roll==542):
        outcome = "Possessive"
    elif(roll==543):
        outcome = "Power-hungry"
    elif(roll==544):
        outcome = "Predatory"
    elif(roll==545):
        outcome = "Prejudiced"
    elif(roll==546):
        outcome = "Presumptuous"
    elif(roll==547):
        outcome = "Pretentious"
    elif(roll==548):
        outcome = "Prim"
    elif(roll==549):
        outcome = "Procrastinating"
    elif(roll==550):
        outcome = "Profligate"
    elif(roll==551):
        outcome = "Provocative"
    elif(roll==552):
        outcome = "Pugnacious"
    elif(roll==553):
        outcome = "Puritanical"
    elif(roll==554):
        outcome = "Quirky"
    elif(roll==555):
        outcome = "Reactionary"
    elif(roll==556):
        outcome = "Reactive"
    elif(roll==557):
        outcome = "Regimental"
    elif(roll==558):
        outcome = "Regretful"
    elif(roll==559):
        outcome = "Repentant"
    elif(roll==560):
        outcome = "Repressed"
    elif(roll==561):
        outcome = "Resentful"
    elif(roll==562):
        outcome = "Ridiculous"
    elif(roll==563):
        outcome = "Rigid"
    elif(roll==564):
        outcome = "Ritualistic"
    elif(roll==565):
        outcome = "Rowdy"
    elif(roll==566):
        outcome = "Ruined"
    elif(roll==567):
        outcome = "Sadistic"
    elif(roll==568):
        outcome = "Sanctimonious"
    elif(roll==569):
        outcome = "Scheming"
    elif(roll==570):
        outcome = "Scornful"
    elif(roll==571):
        outcome = "Secretive"
    elif(roll==572):
        outcome = "Sedentary"
    elif(roll==573):
        outcome = "Selfish"
    elif(roll==574):
        outcome = "Self-indulgent"
    elif(roll==575):
        outcome = "Shallow"
    elif(roll==576):
        outcome = "Shortsighted"
    elif(roll==577):
        outcome = "Shy"
    elif(roll==578):
        outcome = "Silly"
    elif(roll==579):
        outcome = "Single-minded"
    elif(roll==580):
        outcome = "Sloppy"
    elif(roll==581):
        outcome = "Slow"
    elif(roll==582):
        outcome = "Sly"
    elif(roll==583):
        outcome = "Small-thinking"
    elif(roll==584):
        outcome = "Softheaded"
    elif(roll==585):
        outcome = "Sordid"
    elif(roll==586):
        outcome = "Steely"
    elif(roll==587):
        outcome = "Stiff"
    elif(roll==588):
        outcome = "Strong-willed"
    elif(roll==589):
        outcome = "Stupid"
    elif(roll==590):
        outcome = "Submissive"
    elif(roll==591):
        outcome = "Superficial"
    elif(roll==592):
        outcome = "Superstitious"
    elif(roll==593):
        outcome = "Suspicious"
    elif(roll==594):
        outcome = "Tactless"
    elif(roll==595):
        outcome = "Tasteless"
    elif(roll==596):
        outcome = "Tense"
    elif(roll==597):
        outcome = "Thievish"
    elif(roll==598):
        outcome = "Thoughtless"
    elif(roll==599):
        outcome = "Timid"
    elif(roll==600):
        outcome = "Transparent"

    elif(roll==601):
        outcome = "Treacherous"
    elif(roll==602):
        outcome = "Trendy"
    elif(roll==603):
        outcome = "Troublesome"
    elif(roll==604):
        outcome = "Unappreciative"
    elif(roll==605):
        outcome = "Uncaring"
    elif(roll==606):
        outcome = "Uncharitable"
    elif(roll==607):
        outcome = "Unconvincing"
    elif(roll==608):
        outcome = "Uncooperative"
    elif(roll==609):
        outcome = "Uncreative"
    elif(roll==610):
        outcome = "Uncritical"
    elif(roll==611):
        outcome = "Unctuous"
    elif(roll==612):
        outcome = "Undisciplined"
    elif(roll==613):
        outcome = "Unfriendly"
    elif(roll==614):
        outcome = "Ungrateful"
    elif(roll==615):
        outcome = "Unhealthy"
    elif(roll==616):
        outcome = "Unimaginative"
    elif(roll==617):
        outcome = "Unimpressive"
    elif(roll==618):
        outcome = "Unlovable"
    elif(roll==619):
        outcome = "Unpolished"
    elif(roll==620):
        outcome = "Unprincipled"
    elif(roll==621):
        outcome = "Unrealistic"
    elif(roll==622):
        outcome = "Unreflective"
    elif(roll==623):
        outcome = "Unreliable"
    elif(roll==624):
        outcome = "Unrestrained"
    elif(roll==625):
        outcome = "Unself-critical"
    elif(roll==626):
        outcome = "Unstable"
    elif(roll==627):
        outcome = "Vacuous"
    elif(roll==628):
        outcome = "Vague"
    elif(roll==629):
        outcome = "Venal"
    elif(roll==630):
        outcome = "Venomous"
    elif(roll==631):
        outcome = "Vindictive"
    elif(roll==632):
        outcome = "Vulnerable"
    elif(roll==633):
        outcome = "Weak"
    elif(roll==634):
        outcome = "Weak-willed"
    elif(roll==635):
        outcome = "Well-meaning"
    elif(roll==636):
        outcome = "Willful"
    elif(roll==637):
        outcome = "Wishful"
    elif(roll==638):
        outcome = "Zany"
    return outcome




with open("comments_replied_to.txt", "r") as f:
    comments_replied_to = f.read()
    comments_replied_to = comments_replied_to.split("\n")
    comments_replied_to = list(filter(None, comments_replied_to))
subreddit = reddit.subreddit('CenturyofBlood+CenturyofBloodMods+COBEventsTeam')
for comment in subreddit.stream.comments(skip_existing=True):
    try:
        comment.refresh()
    
        if((re.search('/u/manyfacedbot',comment.body,re.IGNORECASE) or re.search('u/manyfacedbot',comment.body,re.IGNORECASE)) and comment.id not in comments_replied_to): #Make sure we're tagged in order to run. Non caps-sensitive.
            comments_replied_to.append(comment.id)



            if(re.search("Roll Baby",comment.body,re.IGNORECASE)):
                roundmessage = ""
                outcome = ""
                multiplesRoll = 0
                complicationRoll = 0
                sexRoll2 = 0
                sexRoll3 = 0
                generalRoll = random.randint(1,1000)
                print("Rolling Baby\n\n---\n")
                
                if(generalRoll < 31):
                    outcome = "Twins/Multiples"
                    multiplesRoll = random.randint(1,1000)
                    complicationRoll = random.randint(1,10)
                    
                elif(generalRoll <= 796):
                    outcome = "Single Child that survives"

                elif(generalRoll <= 897):
                    outcome = "Single Child that survives, mother has a complication"
                    complicationRoll = random.randint(1,10)

                elif(generalRoll <= 968):
                    outcome = "Single Child dies, mother survives"
                    complicationRoll = random.randint(1,10)

                elif(generalRoll <= 985):
                    outcome = "Single Child survives, mother dies"

                else:
                    outcome = "Mother and Child die"

                roundmessage += "General Roll: **{}**\n\n".format(generalRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)

                if(multiplesRoll != 0):
                    if(multiplesRoll <= 25):
                        outcome = "Mother dies, twins survive"
                    elif(multiplesRoll <= 40):
                        outcome = "Mother dies, one twin dies while the other survives"
                    elif(multiplesRoll <= 45):
                        outcome = "Mother and both twins die"
                    elif(multiplesRoll <= 156):
                        outcome = "One twin dies"
                    elif(multiplesRoll <= 175):
                        outcome = "Both twins die"
                    elif(multiplesRoll <= 892):
                        outcome = "Fraternal twins that survive"
                        sexRoll2 = random.randint(1,2)
                    elif(multiplesRoll <= 996):
                        outcome = "Identical twins that survive"
                    else:
                        outcome = "Triplets!"
                        sexRoll2 = random.randint(1,2)
                        sexRoll3 = random.randint(1,2)

                    roundmessage += "Multiples Roll: **{}**\n\n".format(multiplesRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)

                if(complicationRoll != 0):
                    if(complicationRoll <= 3):
                        outcome = "Mother's complication does not affect future fertility"
                    elif(complicationRoll <= 6):
                        outcome = "Mother's future fertility is decreased"
                    elif(complicationRoll <= 8):
                        outcome = "Mother's chance of future stillbirths/miscarriages/maternal death is increased"
                    else:
                        outcome = "Mother is infertile in the future"
                    roundmessage += "Complication Roll: **{}**\n\n".format(complicationRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)

                sexRoll = random.randint(1,2)
                if(sexRoll == 1):
                    outcome = "Male Child"
                else:
                    outcome = "Female Child"
                    
                roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll)
                roundmessage += "**{}**\n\n".format(outcome)

                if (sexRoll2 != 0):
                    if(sexRoll2 == 1):
                        outcome = "Male Child"
                    else:
                        outcome = "Female Child"
                    roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll2)
                    roundmessage += "**{}**\n\n".format(outcome)
                    if (sexRoll3 != 0):
                        if(sexRoll3 == 1):
                            outcome = "Male Child"
                        else:
                            outcome = "Female Child"
                        roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll3)
                        roundmessage += "**{}**\n\n".format(outcome)
                        
                roundmessage += "***\n\n"

                comment.reply(roundmessage)#Post all at once
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



            elif(re.search("Roll Traits",comment.body,re.IGNORECASE)):
                roundmessage = ""
                outcome = ""
                goodRoll = 0
                goodRoll2 = 0
                goodRoll3 = 0
                badRoll = 0
                badRoll2 = 0
                badRoll3 = 0
                genius = False
                beautiful = False
                strong = False
                tall = False
                isValid = False
                weak = False
                dumb = False
                ugly = False
                dwarf = False
                generalRoll = random.randint(1,10)
                print("Rolling Traits")
                

                if(generalRoll == 1):
                    outcome = "Child has a good/neutral characteristic"
                    goodRoll = random.randint(1,100)

                elif(generalRoll == 2):
                    outcome = "Child has a bad/harmful characteristic"
                    badRoll = random.randint(1,100)

                elif(generalRoll == 3):
                    outcome = "Child has both a good and bad characteristic"
                    goodRoll = random.randint(1,100)
                    badRoll = random.randint(1,100)

                else:
                    outcome = "Child has no outstanding characteristics at birth"

                roundmessage += "Characteristic Roll: **{}**\n\n".format(generalRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)


                if(goodRoll != 0):
                    print("Good Roll")
                    if(goodRoll <= 24):
                        outcome = "Child has a genius intellect, or is gifted in a particular field"
                        genius = True
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                    elif(goodRoll <= 34):
                        outcome = "Child is especially attractive/beautiful"
                        beautiful = True
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                    elif(goodRoll <= 56):
                        outcome = "Child has a large size/height"
                        tall = True
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                    elif(goodRoll <= 88):
                        outcome = "Child is especially physically strong"
                        strong = True
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                    elif(goodRoll <= 94):
                        outcome = "Child is on the LGBTQ spectrum"
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                    else:
                        
                        
                        outcome = "Multiple good/neutral characteristics"
                        goodRoll2 = random.randint(1,94)
                        if(goodRoll2 <= 24):
                            outcome = "Child has a genius intellect, or is gifted in a particular field"
                            genius = True
                            goodRoll3 = random.randint(25,94)
                            if(goodRoll3 <= 34):
                                outcome2 = "Child is especially attractive/beautiful"
                                beautiful = True
                            elif(goodRoll3 <= 56):
                                outcome2 = "Child has a large size/height"
                                tall = True
                            elif(goodRoll3 <= 88):
                                outcome2 = "Child is especially physically strong"
                                strong = True
                            else:
                                outcome2 = "Child is on the LGBTQ spectrum"
                            
                        elif(goodRoll2 <= 34):
                            outcome = "Child is especially attractive/beautiful"
                            beautiful = True
                            goodroll3 = random.randint(1,94)
                            while (goodRoll3 >= 25 and goodRoll3 <= 34):
                                goodRoll3 = random.randint(1,94)
                            if(goodRoll3 <= 24):
                                outcome2 = "Child has a genius intellect, or is gifted in a particular field"
                                genius = True
                            elif(goodRoll3 <= 56):
                                outcome2 = "Child has a large size/height"
                                tall = True
                            elif(goodRoll3 <= 88):
                                outcome2 = "Child is especially physically strong"
                                strong = True
                            else:
                                outcome2 = "Child is on the LGBTQ spectrum"
                                
                        elif(goodRoll2 <= 56):
                            outcome = "Child has a large size/height"
                            tall = True
                            goodroll3 = random.randint(1,94)
                            while (goodRoll3 >= 35 and goodRoll3 <= 56):
                                goodRoll3 = random.randint(1,94)
                            if(goodRoll3 <= 24):
                                outcome2 = "Child has a genius intellect, or is gifted in a particular field"
                                genius = True
                            elif(goodRoll3 <= 34):
                                outcome2 = "Child is especially attractive/beautiful"
                                beautiful = True
                            elif(goodRoll3 <= 88):
                                outcome2 = "Child is especially physically strong"
                                strong = True
                            else:
                                outcome2 = "Child is on the LGBTQ spectrum"
                                
                        elif(goodRoll2 <= 88):
                            outcome = "Child is especially physically strong"
                            strong = True
                            goodroll3 = random.randint(1,94)
                            while (goodRoll3 >= 57 and goodRoll3 <= 88):
                                goodRoll3 = random.randint(1,94)
                            if(goodRoll3 <= 24):
                                outcome2 = "Child has a genius intellect, or is gifted in a particular field"
                                genius = True
                            elif(goodRoll3 <= 34):
                                outcome2 = "Child is especially attractive/beautiful"
                                beautiful = True
                            elif(goodRoll3 <= 56):
                                outcome2 = "Child has a large size/height"
                                tall = True
                            else:
                                outcome2 = "Child is on the LGBTQ spectrum"
                            
                        else:
                            outcome = "Child is on the LGBTQ spectrum"
                            goodroll3 = random.randint(1,88)
                            if(goodRoll3 <= 24):
                                outcome2 = "Child has a genius intellect, or is gifted in a particular field"
                                genius = True
                            elif(goodRoll3 <= 34):
                                outcome2 = "Child is especially attractive/beautiful"
                                beautiful = True
                            elif(goodRoll3 <= 56):
                                outcome2 = "Child has a large size/height"
                                tall = True
                            else:
                                outcome2 = "Child is especially physically strong"
                                strong = True
                                                        
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll2)
                        roundmessage += "**{}**\n\n".format(outcome)
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll3)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome2)
                        

                if(badRoll != 0):
                    print("Bad Roll")
                    while (isValid == False):
                        dwarf = False
                        ugly = False
                        weak = False
                        dumb = False
                        badmessage = ""

                        if(badRoll == 1):
                            outcome = "Child has dwarfism"
                            dwarf = True
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 5):
                            outcome = "Child is blind"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 6):
                            outcome = "Child is deaf"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 9):
                            outcome = "Child is mentally disabled/slow witted"
                            dumb = True
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 33):
                            outcome = "Child is insane/mentally ill"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 38):
                            outcome = "Child is crippled/disabled"
                            weak = True
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 49):
                            outcome = "Child is especially unattractive"
                            ugly = True
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 60):
                            outcome = "Child is infertile in the future"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 82):
                            outcome = "Other physical defect"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        elif(badRoll <= 94):
                            outcome = "Other genetic disorder"
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome)
                        else:
                            
                            outcome = "Multiple good/neutral characteristics"
                            badRoll2 = random.randint(1,94)
                            if(badRoll2 == 1):
                                outcome = "Child has dwarfism"
                                dwarf = True
                                badRoll3 = random.randint(2,94)
                                if(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"
                                    
                            elif(badRoll2 <= 5):
                                outcome = "Child is blind"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 2 and badRoll3 <= 5):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 6):
                                outcome = "Child is deaf"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 == 6):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 9):
                                outcome = "Child is mentally disabled/slow witted"
                                dumb = True
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 7 and badRoll3 <= 9):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"                
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 33):
                                outcome = "Child is insane/mentally ill"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 10 and badRoll3 <= 33):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                  
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 38):
                                outcome = "Child is crippled/disabled"
                                weak = True   
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 34 and badRoll3 <= 38):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                                                 
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 49):
                                outcome = "Child is especially unattractive"
                                ugly = True
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 39 and badRoll3 <= 49):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"
                            elif(badRoll2 <= 60):
                                outcome = "Child is infertile in the future"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 2 and badRoll3 <= 5):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 82):
                                    outcome2 = "Other physical defect"
                                else:
                                    outcome2 = "Other genetic disorder"

                            elif(badRoll2 <= 82):
                                outcome = "Other physical defect"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 2 and badRoll3 <= 5):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 5):
                                    outcome2 = "Child is blind"
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome2 = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                else:
                                    outcome2 = "Other genetic disorder"

                            else:
                                outcome = "Other genetic disorder"
                                badRoll3 = random.randint(2,94)
                                while (badRoll3 >= 2 and badRoll3 <= 5):
                                    badRoll3 = random.randint(1,94)
                                if(badRoll3 == 1):
                                    outcome2 = "Child is dwarfism"
                                    dwarf = True
                                elif(badRoll3 <= 6):
                                    outcome2 = "Child is deaf"
                                elif(badRoll3 <= 9):
                                    outcome2 = "Child is mentally disabled/slow witted"
                                    dumb = True                        
                                elif(badRoll3 <= 33):
                                    outcome2 = "Child is insane/mentally ill"                        
                                elif(badRoll3 <= 38):
                                    outcome2 = "Child is crippled/disabled"
                                    weak = True                           
                                elif(badRoll3 <= 49):
                                    outcome = "Child is especially unattractive"
                                    ugly = True
                                elif(badRoll3 <= 60):
                                    outcome2 = "Child is infertile in the future"
                                else:
                                    outcome2 = "Other physical defect"

                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll2)
                            badmessage += "**{}**\n\n".format(outcome)
                            badmessage += "Bad/Harmful Characteristic Roll: **{}**\n\n".format(badRoll3)
                            badmessage += "**{}**\n\n ***\n\n".format(outcome2)

                        if (tall == True and dwarf == True):
                            isValid = False
                        elif (beautiful == True and ugly == True):
                            isValid = False
                        elif (strong == True and weak == True):
                            isValid = False
                        elif (genius == True and dumb == True):
                            isValid = False
                        else: #Checks here to see if both incompatible traits are present. If they are it just goes through the loop again, only ending when nothing is incompatible
                            isValid = True

                    roundmessage += badmessage

                trait1 = random.randint(1,6)
                trait2 = random.randint(1,6)
                trait3 = random.randint(1,6)
                if(weak == True):
                    strength = 3
                elif(strong == True):
                    strength = 18
                else:
                    strength = trait1+trait2+trait3
                    
                trait1 = random.randint(1,6)
                trait2 = random.randint(1,6)
                trait3 = random.randint(1,6)
                if(ugly == True):
                    attractiveness = 3
                elif(beautiful == True):
                    attractiveness = 18
                else:
                    attractiveness = trait1+trait2+trait3

                trait1 = random.randint(1,6)
                trait2 = random.randint(1,6)
                trait3 = random.randint(1,6)
                if(dumb == True):
                    intelligence = 3
                elif(genius == True):
                    intelligence = 18
                else:
                    intelligence = trait1+trait2+trait3
                    
                trait1 = random.randint(1,6)
                trait2 = random.randint(1,6)
                trait3 = random.randint(1,6)
                sexuality = trait1+trait2+trait3

                roundmessage += "Strength (without parental modifiers): **{}**\n\n".format(strength)
                roundmessage += "Attractiveness (without parental modifiers): **{}**\n\n".format(attractiveness)
                roundmessage += "Intelligence: **{}**\n\n".format(intelligence)
                roundmessage += "Sexuality: **{}**\n\n".format(sexuality)

                trait1 = traits()
                trait2 = traits()
                trait3 = traits()
                while (trait2 == trait1):
                    trait2 = self.traits
                while (trait3 == trait1 or trait3 == trait2):
                    trait3 = self.traits

                roundmessage += "The child is {}, {} and {}".format(trait1, trait2, trait3)

                print("\n---\n")

                comment.reply(roundmessage)#Post all at once
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.


                
            elif(re.search("Roll",comment.body,re.IGNORECASE)):
                battleInfo = re.findall("(\d+)([d])(\d+)([\+\-]?\d*)(.*)",comment.body)
                if(battleInfo):
                    roundmessage= ""
                    for j in battleInfo:
                        bonus = 0
                        noDice = int(j[0]) #(battleInfo.group(1))
                        sizeDice = int(j[2]) #(battleInfo.group(3))
                        if (j[3]):
                            bonus = int(j[3]) #(battleInfo.group(4))
                        else:
                            bonus = 0
                        name = j[4] #battleInfo.group(5)
                        number = 0
                        printedBonus = 0
                        numberBonus = 0
                        runningBonus = "("
            
                        while(noDice != number):     
                            printed = random.randint(1,sizeDice)
                            printedBonus += printed
                            print("Rolling", name, "\n")
                            if (noDice - number == 1):
                                runningBonus += "{})".format(printed)
                            else:
                                runningBonus += "{} + ".format(printed)
                            number += 1

                            
                        printedBonus += bonus
                            
                        if (bonus > 0):
                            roundmessage += "{}d{}+{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                            roundmessage += "\n\n {} + {} \n\n *** \n\n".format(runningBonus,bonus)
                        elif (bonus < 0):
                            roundmessage += "{}d{}{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                            roundmessage += "\n\n {} {} \n\n *** \n\n".format(runningBonus,bonus)
                        elif (noDice > 1):
                            roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                            roundmessage += "\n\n {} \n\n *** \n\n".format(runningBonus)
                        else:
                            roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                            roundmessage += "\n\n *** \n\n"

                    comment.reply(roundmessage)#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                    print("---\n")
              
                else:
                    print ("Improperly formatted roll\n---\n")
                    comment.reply("Improperly formatted Roll. Please format comment as follows: \n \n 1d100 \n \n Roll \n \n tag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




            elif(re.search("Archery",comment.body,re.IGNORECASE)):
                battleInfo = re.findall("(.*) ([\+\-]\d*)",comment.body)
                if(battleInfo):
                    print("Rolling Archery\n\n---")
                    archerymessage = "#Archery Contest\n\n"
                    archerymessage += "*I am a bot managed and run by the r/CenturyOfBlood modteam. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                    archerymessage += "\n \n"
                    archerymessage += "Credits: skulkdan, dino_king88 \n \n"
                    archerymessage += "--- \n \n"
                    roundmessage = ""
                    k = 1

                    for j in battleInfo:
                        k = 1
                        bonus = 0
                        if (j[1]):
                            bonus = int(j[1]) #(battleInfo.group(4))
                        else:
                            bonus = 0
                        name = j[0] #battleInfo.group(5)
                        printedBonus = ''
                        numberBonus = 0
                        points = 0
                        roundmessage = ""
                        printedBonus = "("
                    
                        while(k <= 7):
                            printed = random.randint(1,100)
                            printed = printed+bonus
                            if (printed > 100):
                                printed = 100
                            printedBonus += "{}".format(printed)
                            if (printed <= 50):
                                points = points + 0
                            elif (printed <= 55):
                                points = points + 1
                            elif (printed <= 60):
                                points = points + 2
                            elif (printed <= 65):
                                points = points + 3
                            elif (printed <= 70):
                                points = points + 4
                            elif (printed <= 75):
                                points = points + 5
                            elif (printed <= 80):
                                points = points + 6
                            elif (printed <= 85):
                                points = points + 7
                            elif (printed <= 90):
                                points = points + 8
                            elif (printed <= 95):
                                points = points + 9
                            elif (printed <= 99):
                                points = points + 10
                            else:
                                points = points + 20
                                
                            if(k != 7):
                                printedBonus += ", "
                            

                            k=k+1

                        printedBonus += ")"
                        roundmessage += "**{}** {}: **{} points**".format(name, printedBonus, points)
                        archerymessage += roundmessage
                        archerymessage += "\n \n"


                    comment.reply(archerymessage)#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")

              
                else:
                    print ("Improperly formatted roll")
                    comment.reply("Improperly formatted Roll. Please format comment as follows: \n \n 1d100 \n \n Roll \n \n tag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.

                
            elif(re.search("Naval Battle",comment.body,re.IGNORECASE)):
                Globals.battleType = "Naval"
                battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
                if(battleInfo):
                    print ("Running Naval battle\n")
                    battle = Battle.Battle()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in battle.run(battleInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(60)
                    else:
                        print ("Quick Mode\n")
                        comment.reply(battle.run(battleInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")

                    print("---\n")
                else:
                    print ("Improperly formatted battle\n---\n")
                    comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



                        
            elif(re.search("Land Battle",comment.body,re.IGNORECASE)):
                Globals.battleType = "Land"
                battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
                if(battleInfo):
                    print ("Running Land battle\n")
                    battle = Battle.Battle()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in battle.run(battleInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(60)
                    else:
                        print ("Quick Mode\n")
                        comment.reply(battle.run(battleInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    print("---\n")
                else:
                    print ("Improperly formatted battle\n---\n")
                    comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




            elif(re.search("Ambush",comment.body,re.IGNORECASE)):
                Globals.battleType = "Ambush"
                battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
                if(battleInfo):
                    print ("Running Ambush battle\n")
                    battle = Battle.Battle()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in battle.run(battleInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(60)
                    else:
                        print ("Quick Mode\n")
                        comment.reply(battle.run(battleInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    print("\n---\n")
                else:
                    print ("Improperly formatted battle\n---\n")
                    comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



            elif(re.search("Assault",comment.body,re.IGNORECASE)):
                Globals.battleType = "Assault"
                battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
                if(battleInfo):
                    print ("Running Assault")
                    battle = Battle.Battle()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode")
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in battle.run(battleInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(60)
                    else:
                        print ("Quick Mode\n")
                        comment.reply(battle.run(battleInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    print("---\n")
                else:
                    print ("Improperly formatted battle\n---\n")
                    comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




            elif(re.search("Blunted Duel",comment.body,re.IGNORECASE)):
                Globals.battleType = "Blunted"
                duelInfo = re.match("(.*) ([\+\-]?\d+)(.*)\n+(.*) ([\+\-]?\d+)(.*)",comment.body)
                if(duelInfo):
                    print ("Running Blunted Duel\n")
                    duel = Duel.Duel()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        Globals.resultsMode = False
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in duel.run(duelInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(30)
                        
                    elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                        Globals.resultsMode = True
                        print ("Results Mode\n")
                        comment.reply(duel.run(duelInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    else:
                        Globals.resultsMode = False
                        print ("Quick Mode\n")
                        comment.reply(duel.run(duelInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    print("---\n")
                else:
                    print ("Improperly formatted duel\n---\n")
                    comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.




            elif(re.search("Live Duel",comment.body,re.IGNORECASE)):
                Globals.battleType = "Live"
                duelInfo = re.match("(.*) ([\+\-]?\d+)(.*)\n+(.*) ([\+\-]?\d+)(.*)",comment.body)
                if(duelInfo):
                    print ("Running Live Duel\n")
                    duel = Duel.Duel()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        Globals.resultsMode = False
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in duel.run(duelInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(30)
                        
                    elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                        Globals.resultsMode = True
                        print ("Results Mode\n")
                        comment.reply(duel.run(duelInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    else:
                        Globals.resultsMode = False
                        print ("Quick Mode\n")
                        comment.reply(duel.run(duelInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")

                    print("--- \n")
                else:
                    print ("\nImproperly formatted duel\n--- \n")
                    comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n\ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.



            elif(re.search("Continued Joust",comment.body,re.IGNORECASE)):
                Globals.battleType = "Continued"
                joustInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)",comment.body)
                if(joustInfo):
                    print ("Running Joust\n")
                    joust = Joust.Joust()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        Globals.resultsMode = False
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in joust.run(joustInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(30)
                        
                    elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                        Globals.resultsMode = True
                        print ("Results Mode\n")
                        comment.reply(joust.run(joustInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    else:
                        Globals.resultsMode = False
                        print ("Quick Mode\n")
                        comment.reply(joust.run(joustInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")

                    print("--- \n")
                else:
                    print ("\nImproperly formatted joust\n--- \n")
                    comment.reply("Improperly formatted joust info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n\ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.


                
            elif(re.search("Joust",comment.body,re.IGNORECASE)):
                Globals.battleType = "Joust"
                joustInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)",comment.body)
                if(joustInfo):
                    print ("Running Joust\n")
                    joust = Joust.Joust()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        Globals.resultsMode = False
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in joust.run(joustInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(30)
                        
                    elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                        Globals.resultsMode = True
                        print ("Results Mode\n")
                        comment.reply(joust.run(joustInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    else:
                        Globals.resultsMode = False
                        print ("Quick Mode\n")
                        comment.reply(joust.run(joustInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")

                    print("--- \n")
                else:
                    print ("\nImproperly formatted joust\n--- \n")
                    comment.reply("Improperly formatted joust info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n\ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.



            elif(re.search("Boxing",comment.body,re.IGNORECASE)):
                duelInfo = re.match("(.*) (\d*)\n+(.*) (\d*)",comment.body)
                if(duelInfo):
                    print ("Running Boxing Match\n")
                    box = Boxing.Boxing()
                    if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                        print ("Dramatic Mode\n")
                        lastcomment = comment
                        comments_replied_to.append(lastcomment.id)
                        for roundCount in box.run(duelInfo).split("---"):
                            try:
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            except: #Shouldn't happen too much, but in case we get rate limited.
                                print("Rate limited. Sleeping for 6 minutes.")
                                time.sleep(360)
                                lastcomment = lastcomment.reply(roundCount)
                                comments_replied_to.append(lastcomment.id)
                                with open("comments_replied_to.txt", "w") as f:
                                    for comment_id in comments_replied_to:
                                        f.write(comment_id + "\n")
                            time.sleep(30)
                    else:
                        print ("Quick Mode\n")
                        comment.reply(box.run(duelInfo))#Post all at once
                        with open("comments_replied_to.txt", "w") as f:
                            for comment_id in comments_replied_to:
                                f.write(comment_id + "\n")
                    print("---\n")
                else:
                    print ("Improperly formatted boxing match\n---\n")
                    comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1  Health \n \nName of PC 2  Health \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n \ntag ManyFacedBot")
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.




            else:
                comment.reply("Improperly formatted info. Please state which function you wish to use; Roll, Land Battle, Naval Battle, Ambush, Assault, Boxing, Live Duel, or Blunted Duel")
                print("Improperly formatted info\n---\n")

    except praw.exceptions.ClientException:  # fix for deleted comments
        print('SKIPPING due to ClientException')
        continue

    
