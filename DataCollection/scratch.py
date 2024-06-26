from DataCollection.database import Database, Record

# DB = Database()
#
# # with open('Data\\database.csv', 'w') as outfile:
# #     outfile.write('name,email,phone,website,secured_party,ucc_filing_number,ucc_file_date,ucc_lapse_date,filing_link\n')
# keys = sorted(DB.keys())
# for key in keys:
#     phone = DB[key]['phone']
#     email = DB[key]['email']
#     website = DB[key]['website']
#     mystring = ''
#     mystring += key + ','
#     mystring += DB[key]['email'] + ','
#     mystring += DB[key]['phone'] + ','
#     mystring += DB[key]['website'] + ','
#     for key2 in ['secured_party', 'ucc_filing', 'ucc_start', 'ucc_lapse', 'ucc_suffix']:
#         try:
#             mystring += DB[key][key2] + ','
#         except:
#             mystring += ','
#     # mystring += DB[key]['email'] + ','
#     # mystring += DB[key]['phone'] + ','
#     # mystring += DB[key]['website'] + ','
#     # mystring += DB[key]['secured_party'] + ','
#     # mystring += DB[key]['ucc_filing'] + ','
#     # mystring += DB[key]['ucc_start'] + ','
#     # mystring += DB[key]['ucc_lapse'] + ','
#     # mystring += DB[key]['ucc_suffix'] # + '\n'
#     print(mystring)
#         # outfile.write(mystring)

text = """Processing: a arata sushi
Retrieving:  https://www.facebook.com/aratasushiprospect/about
Got phone:  ['(502)409-4880']
Got email:  aratasushiprospect@gmail.com
Got website:  aratasushiprospect.com/
Retrieving:  https://m.facebook.com/aratasushiprospect/photos/about
Got phone:  
Got email:  
Got website:  
Processing: a b c d partnership
Processing: a b c rental center inc
Processing: a b interior design
Retrieving:  https://www.facebook.com/p/A-B-Interior-Design-100063694657031/about
Redirecting to:  https://www.facebook.com/p/A-B-Interior-Design-100063694657031/?sk=about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/A-B-Interior-Design-414021970453/?locale=fr_FRabout
Got phone:  ['(606)874-9611']
Got email:  brenda_may@bellsouth.net
Got website:  abinterior.houzz.com
Processing: a b steel buildings inc
Processing: a barry klein md
Processing: a bayus inc
Processing: a better view ministries inc
Processing: a blair enterprises inc
Retrieving:  https://m.facebook.com/ablairenterprises/photos/about
Got phone:  
Got email:  
Got website:  
Processing: a book company llc
Processing: a brandon denton
Retrieving:  https://www.facebook.com/brandon.denton.796/about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/brandon.denton.5496/about
Got phone:  
Got email:  
Got website:  
Processing: a brides dream llc
Retrieving:  https://www.facebook.com/abridalpromandpageantshop/about
Got phone:  ['(502)345-3180']
Got email:  bridalandprom@yahoo.com
Got website:  
Retrieving:  https://www.facebook.com/EveryBridesDream/about
Got phone:  
Got email:  everybridesdreamllc@gmail.com
Got website:  
Processing: a g exhibitions inc
Processing: a brighter future inc
Retrieving:  https://www.facebook.com/abfinc/about
Got phone:  ['(606)845-7905']
Got email:  goldenpoppysandiego@gmail.com
Got website:  abrighterfuture.com/
Retrieving:  https://m.facebook.com/profile.php?id=306820543332794about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/profile.php?id=306820543332794about
Got phone:  
Got email:  
Got website:  
Processing: a business solutions company
Processing: a business solutions company llc
Retrieving:  https://www.facebook.com/cdavisconsulting1/about
Got phone:  ['(856)537-8701']
Got email:  cdavis@yourtopbusinesssolutions.com
Got website:  yourtopbusinesssolutions.com/
Retrieving:  https://www.facebook.com/YourBusinessSolutionLLC/about
Got phone:  ['(802)923-9134']
Got email:  ybs.denovellis@gmail.com
Got website:  
Processing: a buyers choice llc
Retrieving:  https://www.facebook.com/ABCHIUSA/about
Got phone:  ['(800)929-0189']
Got email:  join@abuyerschoice.com
Got website:  abuyerschoice.com/join/
Retrieving:  https://www.facebook.com/ABCHIMartin/about
Got phone:  ['(772)932-9009']
Got email:  jeff.moores@abuyerschoice.com
Got website:  martincounty.abuyerschoice.com/
Processing: a c krebs company
Processing: a c new partnership
Processing: a caring touch pediatrics and international adoptions pllc
Processing: a center 4 change
Retrieving:  https://m.facebook.com/p/A-Center-4-Change-Counseling-100042873386575/about
Redirecting to:  https://m.facebook.com/p/A-Center-4-Change-Counseling-100042873386575/?sk=about
Got phone:  ['(606)475-0334']
Got email:  
Got website:  acenter4change.com
Processing: a center 4 change counseling and psychotherapy incorporated
Retrieving:  https://m.facebook.com/p/A-Center-4-Change-Counseling-100042873386575/about
Redirecting to:  https://m.facebook.com/p/A-Center-4-Change-Counseling-100042873386575/?sk=about
Got phone:  ['(606)475-0334']
Got email:  
Got website:  acenter4change.com
Processing: a center for change
Retrieving:  https://www.facebook.com/center4change/about
Got phone:  ['(888)224-8250']
Got email:  info@centerforchange.com
Got website:  centerforchange.com/
Processing: a choice dental care pllc
Retrieving:  https://m.facebook.com/p/A-Choice-Dental-Care-Pllc-100063728601423/about
Redirecting to:  https://m.facebook.com/p/A-Choice-Dental-Care-Pllc-100063728601423/?sk=about
Got phone:  ['(502)895-1171']
Got email:  
Got website:  achoicedentalcare.com
Processing: a clean beyond inc
Retrieving:  https://m.facebook.com/p/Beyond-Clean-Inc-100078017890810/about
Redirecting to:  https://m.facebook.com/p/Beyond-Clean-Inc-100078017890810/?sk=about
Got phone:  ['(314)200-6900']
Got email:  
Got website:  beyondcleanstl.com
Retrieving:  https://www.facebook.com/BeyondCleanPodcast/about
Got phone:  
Got email:  info@beyondclean.net
Got website:  beyondcleanmedia.com/
Processing: a complete rental llc
Retrieving:  https://www.facebook.com/stanfordrental/about
Got phone:  ['(606)365-8665']
Got email:  jt.howard@hotmail.com
Got website:  lincolnequipmentrental.com/
Processing: a crouse
Processing: a cup of common wealth llc
Retrieving:  https://www.facebook.com/CupGeorgetown/about
Got phone:  ['(859)255-0270']
Got email:  info@acupofcommonwealth.com
Got website:  acupofcommonwealth.com/
Retrieving:  https://www.facebook.com/CupGeorgetown/about
Got phone:  ['(859)255-0270']
Got email:  info@acupofcommonwealth.com
Got website:  acupofcommonwealth.com/
Retrieving:  https://www.facebook.com/CupGeorgetown/about
Got phone:  ['(859)255-0270']
Got email:  info@acupofcommonwealth.com
Got website:  acupofcommonwealth.com/
Processing: a cut above lawn care service inc
Retrieving:  https://www.facebook.com/ACutAbove81/about
Got phone:  ['(606)776-2655']
Got email:  jeremy.d.perry27@gmail.com
Got website:  
Retrieving:  https://www.facebook.com/ACutAboveBG/about
Got phone:  ['(270)842-4781']
Got email:  
Got website:  cutabovelawnbg.com/
Processing: a cut above tree service and more    llc
Processing: a cut above tree service and more llc
Processing: a d porter and sons south-east llc
Processing: a d s and associates inc
Processing: a d x transportation inc
Processing: a day in time llc
Retrieving:  https://www.facebook.com/ADayInTime/about
Got phone:  ['(270)993-5587']
Got email:  
Got website:  
Processing: a diamond in the ruff
Retrieving:  https://www.facebook.com/ADITRUFF/about
Got phone:  ['(406)750-2529']
Got email:  
Got website:  adiamondintheruffgf.com/
Processing: a e nikki corporation
Retrieving:  https://www.facebook.com/p/Nikki-and-Company-Hair-Design-Boutique-100034369102224/about
Redirecting to:  https://www.facebook.com/p/Nikki-and-Company-Hair-Design-Boutique-100034369102224/?sk=about
Got phone:  
Got email:  
Got website:  
Processing: a f winstead and j m rocha
Processing: a feldmann tax service
Retrieving:  https://m.facebook.com/2957560267634555/about
Got phone:  
Got email:  
Got website:  
Processing: a festive touch
Retrieving:  https://www.facebook.com/festivetouch/about
Got phone:  
Got email:  
Got website:  
Processing: a gentlemens cut
Retrieving:  https://www.facebook.com/festivetouch/about
Got phone:  
Got email:  
Got website:  
Processing: a gentlemens cut llc
Retrieving:  https://m.facebook.com/GentlemenHairCutsLLC/posts/561851888854267/?comment_id=454090973268912about
Got phone:  
Got email:  
Got website:  
Processing: a george s ilnick painting
Processing: a gomez transport llc
Retrieving:  https://www.facebook.com/gomeztransport/about
Got phone:  ['(775)293-2825']
Got email:  gomeztransportllc@hotmail.com
Got website:  
Processing: a h trucking limited liability company
Retrieving:  https://www.facebook.com/ahtruckingllc/about
Got phone:  ['(417)442-3741']
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/IAHfreight/about
Got phone:  ['(732)986-7066']
Got email:  iahfreight@gmail.com
Got website:  
Processing: a himalaya ky properties llc
Retrieving:  https://www.facebook.com/HimalayaProperties9686/about
Got phone:  ['(270)779-9686']
Got email:  support@himalayaproperties.org
Got website:  
Retrieving:  https://m.facebook.com/HimalayaProperties9686/photos/about
Got phone:  
Got email:  
Got website:  
Processing: a himalaya ky2 properties llc
Retrieving:  https://www.facebook.com/HimalayaProperties9686/about
Got phone:  ['(270)779-9686']
Got email:  support@himalayaproperties.org
Got website:  
Retrieving:  https://m.facebook.com/HimalayaProperties9686/photos/about
Got phone:  
Got email:  
Got website:  
Processing: a himalaya usa properties llc
Retrieving:  https://www.facebook.com/HimalayaProperties9686/about
Got phone:  ['(270)779-9686']
Got email:  support@himalayaproperties.org
Got website:  
Processing: a i a agency inc
Retrieving:  https://www.facebook.com/TheAgencyInc.Talent.Models/about
Got phone:  ['(501)374-6447']
Got email:  casting@theagencyinc.com
Got website:  theagencyinc.com/
Processing: a j seibert co inc
Processing: a jungbert company
Retrieving:  https://m.facebook.com/JungbertCompany/about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/JungbertCompany/?locale=ms_MYabout
Got phone:  ['(502)595-9895']
Got email:  charles.jungbert@jungbertcompany.com
Got website:  www.jungbertcompany.com
Processing: a k a trucking company
Processing: a l johnson distributor llc
Processing: a l johnson distributors llc
Processing: a l pickens co inc
Processing: a l turner and son llc
Retrieving:  https://m.facebook.com/p/Turner-Sons-Roofing-Siding-LLC-100063892426905/about
Redirecting to:  https://m.facebook.com/p/Turner-Sons-Roofing-Siding-LLC-100063892426905/?sk=about
Got phone:  ['(860)346-7405']
Got email:  
Got website:  turnerandsonsllc.com
Processing: a lakin and sons inc
Processing: a little bit personal
Retrieving:  https://www.facebook.com/ALittleBitofPersonalStyle/about
Got phone:  ['(859)588-5546']
Got email:  alittlebitofpersonalstyle@yahoo.com
Got website:  alittlebitofpersonalstyle.com/
Processing: a little bliss pllc
Retrieving:  https://www.facebook.com/ALittleBlissMedSpa/about
Got phone:  ['(859)533-1450']
Got email:  
Got website:  
Processing: a little miracle child development center inc
Retrieving:  https://www.facebook.com/p/A-Little-Miracle-Cdc-100063820980701/about
Redirecting to:  https://www.facebook.com/p/A-Little-Miracle-Cdc-100063820980701/?sk=about
Got phone:  
Got email:  
Got website:  
Processing: a lumper relocation labor service
Retrieving:  https://www.facebook.com/alumperlabor/about
Got phone:  
Got email:  
Got website:  alumper.com/
Processing: a m electrical services inc
Retrieving:  https://www.facebook.com/AMElectricalContractor/about
Got phone:  ['(631)208-1739']
Got email:  a_melectrical@yahoo.com
Got website:  eastendelectricalcontractor.com/
Retrieving:  https://www.facebook.com/p/Electric-Services-Inc-100083522102548/about
Redirecting to:  https://www.facebook.com/p/Electric-Services-Inc-100083522102548/?sk=about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/p/Electric-Services-Inc-100083522102548/about
Redirecting to:  https://www.facebook.com/p/Electric-Services-Inc-100083522102548/?sk=about
Got phone:  
Got email:  
Got website:  
Processing: a m skincare inc
Retrieving:  https://www.facebook.com/ambeautyinc/about
Got phone:  ['(920)475-1157']
Got email:  am.beauty.incorporated@gmail.com
Got website:  
Retrieving:  https://www.facebook.com/Skincareinc/about
Got phone:  
Got email:  salon@skincareinc.co.uk
Got website:  
Processing: a m y j truck llc
Retrieving:  https://www.facebook.com/meandmytruck/?locale=fr_CAabout
Got phone:  ['(440)897-3001']
Got email:  info@meandmytruck.net
Got website:  
Retrieving:  https://m.facebook.com/theplanttruckllc/?locale=fr_CAabout
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/theplanttruckllc/?locale=fr_CAabout
Got phone:  
Got email:  
Got website:  
Processing: a mortgage solution 4u inc
Processing: a mothers way corporation
Retrieving:  https://www.facebook.com/Mothers.Way/about
Got phone:  
Got email:  
Got website:  mothersway.com.ph/
Retrieving:  https://www.facebook.com/mothersway.for.japan/about
Got phone:  
Got email:  info@mothersway.jp
Got website:  
Retrieving:  https://www.facebook.com/mothersway.for.japan/videos/interview-/1666829890029871/about
Got phone:  
Got email:  
Got website:  japan series part 19: seryosong usapan tayo tungkol sa gastos at reserve status sa japan. handa ka na bang malaman? 🤔💼 watch now! 🎥🔍 youtube.com/watch?v=4izykbcivs0&t=18s have any more questions in mind? 🤔 feel free to comment down below. we will try to answer them and help you understand more. study nihongo: facebook.com/connectnihongoph rent yukata: facebook.com/japanatin-yukata #japanatin #japan #work #travel #study #howmuch #reserve #reservestatus #resereveemployee #hired
Retrieving:  https://www.facebook.com/mothersway.for.japan/videos/969088360445951/about
Got phone:  
Got email:  
Got website:  japan series part 19: seryosong usapan tayo tungkol sa gastos at reserve status sa japan. handa ka na bang malaman? 🤔💼 watch now! 🎥🔍 youtube.com/watch?v=4izykbcivs0&t=18s have any more questions in mind? 🤔 feel free to comment down below. we will try to answer them and help you understand more. study nihongo: facebook.com/connectnihongoph rent yukata: facebook.com/japanatin-yukata #japanatin #japan #work #travel #study #howmuch #reserve #reservestatus #resereveemployee #hired
Retrieving:  https://www.facebook.com/mothersway.for.japan/videos/2237714353077886/about
Got phone:  
Got email:  
Got website:  japan series part 19: seryosong usapan tayo tungkol sa gastos at reserve status sa japan. handa ka na bang malaman? 🤔💼 watch now! 🎥🔍 youtube.com/watch?v=4izykbcivs0&t=18s have any more questions in mind? 🤔 feel free to comment down below. we will try to answer them and help you understand more. study nihongo: facebook.com/connectnihongoph rent yukata: facebook.com/japanatin-yukata #japanatin #japan #work #travel #study #howmuch #reserve #reservestatus #resereveemployee #hired
Retrieving:  https://www.facebook.com/mothersway.for.japan/videos/housekeeper-ironing-training/796658540853154/about
Got phone:  
Got email:  
Got website:  japan series part 19: seryosong usapan tayo tungkol sa gastos at reserve status sa japan. handa ka na bang malaman? 🤔💼 watch now! 🎥🔍 youtube.com/watch?v=4izykbcivs0&t=18s have any more questions in mind? 🤔 feel free to comment down below. we will try to answer them and help you understand more. study nihongo: facebook.com/connectnihongoph rent yukata: facebook.com/japanatin-yukata #japanatin #japan #work #travel #study #howmuch #reserve #reservestatus #resereveemployee #hired
Processing: a mri llc
Retrieving:  https://www.facebook.com/ldcmri1/about
Got phone:  ['(859)278-7226']
Got email:  m.hancock@ldcmri.com
Got website:  lexingtondiagnostic.com/
Processing: a myers davis dev co inc
Retrieving:  https://www.facebook.com/MyersDavisLC/about
Got phone:  ['(870)569-1052']
Got email:  myersdavis@myersdavis.com
Got website:  myersdavis.com/
Processing: a n a transport llc
Processing: a new beginning consignment
Processing: a new direction llc
Retrieving:  https://m.facebook.com/p/A-New-Direction-Counseling-LLC-100070094982562/about
Redirecting to:  https://m.facebook.com/p/A-New-Direction-Counseling-LLC-100070094982562/?sk=about
Got phone:  
Got email:  
Got website:  
Processing: a new dream llc
Retrieving:  https://www.facebook.com/anewdreamllc/about
Got phone:  
Got email:  anewdreamllc@gmail.com
Got website:  
Processing: a new leaf flowers gifts and more a ky limited liability company
Retrieving:  https://www.facebook.com/anewleaf.ky/about
Got phone:  ['(270)997-1643']
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/photo/?fbid=842901464303488&set=pcb.842903080969993about
Got phone:  
Got email:  
Got website:  
Processing: a new leaf newport inc
Retrieving:  https://www.facebook.com/anewleafnewport/about
Got phone:  ['(859)581-8700']
Got email:  anewleafnewport@gmail.com
Got website:  anewleafnewport.com/
Retrieving:  https://m.facebook.com/anewleafnewport/?locale=fr_FRabout
Processing: a new leaf flowers gifts and more a ky limited liability company
Retrieving:  https://www.facebook.com/anewleaf.ky/about
Got phone:  ['(270)997-1643']
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/photo/?fbid=842901464303488&set=pcb.842903080969993about
Got phone:  
Got email:  
Got website:  
Processing: a new leaf newport inc
Retrieving:  https://www.facebook.com/anewleafnewport/about
Got phone:  ['(859)581-8700']
Got email:  anewleafnewport@gmail.com
Got website:  anewleafnewport.com/
Processing: a new start ii
Retrieving:  https://www.facebook.com/ANewStartClinic/about
Got phone:  ['(866)934-4611']
Got email:  support@ansclinic.com
Got website:  anewstartclinics.com/
Processing: a new start ii llc
Retrieving:  https://www.facebook.com/ANewStartClinic/about
Got phone:  ['(866)934-4611']
Got email:  support@ansclinic.com
Got website:  anewstartclinics.com/
Processing: a newco llc
Processing: a one pallet
Retrieving:  https://m.facebook.com/profile.php?id=583383455053886about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/profile.php?id=568673436515782about
Got phone:  
Got email:  
Got website:  
Processing: a one pallet  inc
Retrieving:  https://www.facebook.com/unitedpallet/?locale=uk_UAabout
Got phone:  ['(209)538-5844']
Got email:  office@unitedpalletservices.com
Got website:  unitedpalletservices.com
Processing: a one pallet inc
Retrieving:  https://m.facebook.com/profile.php?id=583383455053886about
Got phone:  
Got email:  
Got website:  
Processing: a one pallet inc aka one pallet distributing inc
Retrieving:  https://m.facebook.com/profile.php?id=583383455053886about
Got phone:  
Got email:  
Got website:  
Processing: a p hill properties
Processing: a p hill properties llc
Retrieving:  https://m.facebook.com/p/Thomas-Hill-Properties-LLC-100057535295661/?locale=hi_INabout
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/p/Thomas-Hill-Properties-LLC-100057535295661/?locale=hi_INabout
Got phone:  
Got email:  
Got website:  
Processing: a p nahra inc
Processing: a p schweitzer insurance agency inc
Processing: a p schweitzer tax service inc
Processing: a painter llc
Retrieving:  https://www.facebook.com/bluegrasspaintingllc/about
Got phone:  ['(859)967-8745']
Got email:  mcgee@bluegrasspainting.com
Got website:  bluegrasspaintinglexingtonky.com/
Retrieving:  https://www.facebook.com/painterpainterllc/about
Got phone:  ['(864)384-6553']
Got email:  wpainter28@gmail.com
Got website:  
Processing: a place for you inc
Processing: a place for you salon llc
Retrieving:  https://www.facebook.com/AplaceforyousalonandBoutique/about
Got phone:  ['(502)384-3110']
Got email:  aplaceforyousalon@gmail.com
Got website:  vagaro.com/aplaceforyousalon
Retrieving:  https://www.facebook.com/AllAboutYou301/about
Got phone:  ['(502)348-1100']
Got email:  allaboutyou.bardstown.ky@gmail.com
Got website:  allaboutyou301.wixsite.com/allaboutyou
Processing: a plus accounting and tax service inc
Retrieving:  https://www.facebook.com/aplusaccountingandtaxservices/about
Got phone:  ['(757)596-8062']
Got email:  maryann@aplusat.com
Got website:  
Retrieving:  https://m.facebook.com/p/A-Plus-Accounting-Tax-Services-100057056185354/about
Redirecting to:  https://m.facebook.com/p/A-Plus-Accounting-Tax-Services-100057056185354/?sk=about
Got phone:  ['(717)737-4004']
Got email:  
Got website:  kdtaxhub.com
Processing: a plus auto llc
Retrieving:  https://m.facebook.com/p/A-Plus-Auto-Sales-100083070352196/about
Redirecting to:  https://m.facebook.com/p/A-Plus-Auto-Sales-100083070352196/?sk=about
Got phone:  
Got email:  
Got website:  aplusautocar.com
Processing: a plus computers
Retrieving:  https://m.facebook.com/p/A-Plus-Computers-100066290093542/about
Redirecting to:  https://m.facebook.com/p/A-Plus-Computers-100066290093542/?sk=about
Got phone:  ['(864)220-4211']
Got email:  
Got website:  
Processing: a plus contractors llc
Retrieving:  https://www.facebook.com/apluscontractorsky/about
Got phone:  ['(606)932-2222']
Got email:  info@aplusgenerators.us
Got website:  
Processing: a plus paper shredding inc
Retrieving:  https://m.facebook.com/apluspapershredding/?locale=ms_MYabout
Got phone:  
Got email:  
Got website:  
Processing: a plus primetime
Retrieving:  https://www.facebook.com/primetimeshopping/about
Got phone:  ['(855)474-6778']
Got email:  customerservice@4shoppts.com
Got website:  primetimeshopping.com/
Processing: a plus primetimellc
Processing: a plus refrigeration and appliance service
Retrieving:  https://www.facebook.com/RobAplusapplianceguru/about
Got phone:  ['(502)631-9731']
Got email:  aratedappliancerepair@yahoo.com
Got website:  aplusappliancerepairservice.com/
Retrieving:  https://www.facebook.com/APlusApplianceServicesLtd/about
Got phone:  
Got email:  
Got website:  
Processing: a plus residential services llc
Retrieving:  https://www.facebook.com/apluservices/about
Got phone:  ['(571)287-9277']
Got email:  info@aplus-servicesllc.net
Got website:  
Retrieving:  https://www.facebook.com/AllResidentialService/about
Got phone:  ['(319)464-7631']
Got email:  info@allresidentialservice.com
Got website:  allresidentialservice.com/
Processing: a plus signs and screen printing llc
Retrieving:  https://www.facebook.com/APlusSignsAndScreenPrint/?locale=en_GBabout
Got phone:  
Got email:  design@apluskentucky.com
Got website:  apluskentucky.com
Retrieving:  https://www.facebook.com/APlusSignsAndScreenPrint/?locale=en_GBabout
Got phone:  
Got email:  design@apluskentucky.com
Got website:  apluskentucky.com
Processing: a plus transport inc
Retrieving:  https://www.facebook.com/aplustransportservices/about
Got phone:  
Got email:  info@aplustransportservices.com
Got website:  aplustransportservices.com/
Processing: a plus transport llc
Retrieving:  https://www.facebook.com/aplustransportllc/about
Got phone:  ['(704)288-9748']
Got email:  aplustransportrides@gmail.com
Got website:  aplustransportrides.com/vehicles
Retrieving:  https://www.facebook.com/Primetransportky/about
Got phone:  ['(727)900-6979']
Got email:  primetransportky@gmail.com
Got website:  
Processing: a plush lawn llc
Retrieving:  https://www.facebook.com/Plush.Lawn.LLC/about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/Plush.Lawn.LLC/photos/?ref=page_internalabout
Got phone:  
Got email:  
Got website:  
Processing: a polston holdings llc
Processing: a professional tree service inc
Retrieving:  https://www.facebook.com/p/A-Professional-Tree-Service-100045004554957/about
Redirecting to:  https://www.facebook.com/p/A-Professional-Tree-Service-100045004554957/?sk=about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://m.facebook.com/pages/A-Professional-Tree-Service/362472467590240/?locale=ms_MYabout
Got phone:  
Got email:  
Got website:  
Processing: a r long inc
Retrieving:  https://www.facebook.com/WRLONGNC/about
Got phone:  ['(252)823-4570']
Got email:  jnabb@wrlonginc.com
Got website:  wrlonginc.com/
Processing: a roberts and associates inc
Retrieving:  https://m.facebook.com/watch/834394036700674/about
Got phone:  
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/p/A-Roberts-Associates-Inc-100064823328413/?locale=eu_ESabout
Got phone:  ['(888)955-3665']
Got email:  info@arobertsassociates.com
Got website:  arobertsassociates.com
Processing: a s express limited liability company
Retrieving:  https://www.facebook.com/p/RS-Express-LLC-100064281334336/about
Redirecting to:  https://www.facebook.com/p/RS-Express-LLC-100064281334336/?sk=about
Got phone:  
Got email:  
Got website:  
Processing: a s hukle management llc
Processing: a s l excavating inc
Retrieving:  https://www.facebook.com/TLExcavatingAndPavingInc/posts/1322256967791237/about
Got phone:  
Got email:  
Got website:  
Processing: a sandoval
Processing: a sherman buschemeyer llc
Processing: a sherman bushemeyer llc
Processing: a showcase real estate group llc
Retrieving:  https://m.facebook.com/p/A-ShowCase-Real-Estate-Group-LLC-100076187227737/about
Redirecting to:  https://m.facebook.com/p/A-ShowCase-Real-Estate-Group-LLC-100076187227737/?sk=about
Got phone:  ['(859)209-2017']
Got email:  
Got website:  
Retrieving:  https://www.facebook.com/p/A-ShowCase-Real-Estate-Group-LLC-100076187227737/?locale=tl_PHabout
Got phone:  ['(859)209-2017']
Got email:  centralkyrealtysales@gmail.com
Got website:  
Processing: a simple touch aesthetics pllc
Retrieving:  https://www.facebook.com/preferredaesthetics4u/about
Got phone:  ['(919)268-0646']
Got email:  angela@preferredaesthetics.com
Got website:  preferred-aesthetics.com/"""

def main():
    data = text.split('\n')
    name, email, phone, website = '', '', '', ''
    for line in data:
        if line.startswith('Processing: '):
            phone = phone.replace(' ', '')
            email = email.replace(' ', '')
            website = website.replace(' ', '')
            name = line[12:]
        if line.startswith('Got phone: '):
            phone = line[14:-2]
        if line.startswith('Got email: '):
            email = line[11:]
        if line.startswith('Got website: '):
            website = line[13:]
            if phone or email or website:
                print(f'{name},{email},{phone},{website}')
                name, email, phone, website = '', '', '', ''
        # print(line)

def main2():
    f = open('C:\\Users\\pvshe\\Desktop\\temp3.txt', 'r')
    data = f.readlines()
    f.close()
    for i in data:
        if 'Processing' in i:
            continue
        if 'Updated' in i:
            continue
        print(i[:-5])

def main3():
    # The one with old entries
    f1 = open('C:\\Users\\pvshe\\Downloads\\file1.csv', 'r')
    # The one with new entries
    f2 = open('C:\\Users\\pvshe\\Downloads\\file2.csv', 'r')

    data1 = [i[:-1] for i in f1.readlines()]
    data2 = [i[:-1] for i in f2.readlines()]
    f1.close()
    f2.close()

    outfile = open('C:\\Users\\pvshe\\Desktop\\nodupes.csv', 'w')

    for i in data2:
        if i not in data1:
            outfile.write(i + '\n')

    outfile.close()


main3()