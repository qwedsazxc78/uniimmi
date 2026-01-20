# 國籍法-全國法規資料庫

Source: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0030001

Fetched (UTC): 2026-01-20T05:33:46Z

HTTP status: 200

---

國籍法-全國法規資料庫

 .line-0000 {margin-left: 1em; text-indent: -0em;}
.line-0004 {margin-left: 3em; text-indent: -2em;}

 try {
 if (top.location.host != window.location.host)
 top.location = window.location;
 }
 catch (err) {
 top.location = window.location;
 }

 window.dataLayer = window.dataLayer || [];
 function gtag() { dataLayer.push(arguments); }
 gtag('js', new Date());
 gtag('config', 'G-QFLS1G3FEY', { cookie_flags: 'max-age=7200;SameSite=Strict;Secure' });

 您的瀏覽器，不支援javascript script語法，恐影響到網頁的閱讀 

 跳至主要內容 

 ::: 
 網站導覽 
 English 
 會員登入 

 小字型 
 中字型 
 大字型 

 整合查詢 

 整合查詢 
 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 智慧查找 

 熱門詞彙： 刑法 、 職業安全衛生 、 勞基法 、 憲法 、 採購法 

 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 綜合查詢 
 跨機關檢索 

 熱門法規 
 相關連結 
 網站導覽 
 English 
 會員登入 

 ::: 

 現在位置：
 首頁 
 中央法規 
 所有條文 

 P 

 $(function () {
 $(".share-bar").css("display", "inline-block");
 $(".share-bar a").on("click keypress ", function (event) {
 if (event.keyCode == 13 || event.button == 0) {
 event.preventDefault();
 var Type = $(this).data("sharetype");
 if (Type != "PDF")
 window.open(shareTo(Type, "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0030001"), "_blank");
 else window.location.href = $('#hlkPdf').attr("href");
 }
 });
 });

 下載 
 友善列印 

 加入資料夾： 

 儲存 

 確定 
 新增資料夾 
 管理資料夾 

 $(function () {
 //無障礙，預設隱藏，JS有啟用時才看的到
 $("#hlAddToFolder").removeClass("hidden");
 $(".folder-menu li").last().hide();
 $("#hlNewFolder").on("click", function (event) {
 event.preventDefault();
 $(".folder-menu li").last().toggle();
 if ($(this).text() == "新增資料夾") {
 $("#txtNewFolder").focus();
 $(this).text("取消");
 }
 else
 $(this).text("新增資料夾");
 });
 $("#btnAddNewFolder").on("click", function (event) {
 var fname = $.trim($("#txtNewFolder").val());
 if (fname == "") return false;

 $.ajax({
 url: "../controls/FolderHandler.ashx",
 type: "POST",
 dataType: "json",
 data: {
 foldername: encodeURI($.trim($("#txtNewFolder").val()))
 },
 success: function (data) {

 $.each(data, function (index, element) {
 $(" " + element.NAME + " ")
 .insertBefore($("#folderlist li:last"));
 $("#txtNewFolder").val("");
 $(".folder-menu li").last().hide();
 });
 }
 });
 });
 $("#hlSaveToFolder").on("click", function (event) {
 var checkedFID = $("#folderlist input[type='checkbox']:checked").map(function () { return this.value; }).get().join(',');
 if (checkedFID == "") {
 alert("請選擇所要儲存的資料夾。")
 return false;
 }
 $.ajax({
 url: "../controls/FolderHandler.ashx",
 type: "POST",
 data: {
 lan: "C",
 datatype: encodeURI("01"),
 dataid: encodeURI("D0030001"),
 datatitle: encodeURI("國籍法"),
 fid: encodeURI(checkedFID)
 },
 success: function (data) {
 alert("您已成功儲存此頁至您個人資料夾。");
 $("#folderlist input[type='checkbox']").prop("checked", false);
 $("#folderlist").collapse("hide");
 }
 });
 });
 $('#hlMoveToFolder').on("click", function () {
 var x = $('#hfSelect').val();
 var checkedFID = $("#folderlist input[type='checkbox']:checked").map(function () { return this.value; }).get().join(',');
 if (checkedFID == "") {
 alert("請選擇所要儲存的資料夾。")
 return false;
 }
 if (x=='') {
 alert("請選擇所要搬移的資料。")
 return false;
 }
 $.ajax({
 url: "../controls/FolderMoveHandler.ashx",
 type: "POST",
 data: {
 rfid: encodeURI(''),
 did: encodeURI(x),
 fid: encodeURI(checkedFID)
 },
 success: function (data) {
 alert("您已成功儲存此頁至您個人資料夾。");
 $("#folderlist input[type='checkbox']").prop("checked", false);
 $("#folderlist").collapse("hide");
 window.location.reload();
 }
 });
 });
 });

 所有條文 

 法規名稱： 

 國籍法 
 EN 

 修正日期： 
 民國 113 年 05 月 24 日 

 法規類別： 
 行政 ＞ 內政部 ＞ 戶政目 

 所有條文 

 條號查詢 
 條文檢索 
 授權子法 
 沿革 

 立法歷程(附帶決議) 

 ※如已配合行政院組織改造，公告變更管轄或停止辦理業務之法規條文，請詳見沿革 

 第 1 條 
 中華民國國籍之取得、喪失、回復與撤銷，依本法之規定。 

 第 2 條 
 有下列各款情形之一者，屬中華民國國籍： 一、出生時父或母為中華民國國民。 二、出生於父或母死亡後，其父或母死亡時為中華民國國民。 三、出生於中華民國領域內，父母均無可考，或均無國籍者。 四、歸化者。 前項第一款及第二款規定，於本法中華民國八十九年二月九日修正施行時未滿二十歲之人，亦適用之。 

 第 3 條 
 外國人或無國籍人，現於中華民國領域內有住所，並具備下列各款要件者，得申請歸化： 一、於中華民國領域內，每年合計有一百八十三日以上合法居留之事實繼續五年以上。 二、依中華民國法律及其本國法均有行為能力。 三、無不良素行，且無警察刑事紀錄證明之刑事案件紀錄。 四、有相當之財產或專業技能，足以自立，或生活保障無虞。 五、具備我國基本語言能力及國民權利義務基本常識。 前項第三款所定無不良素行，其認定、邀集專家學者及社會公正人士研議程序、定期檢討機制及其他應遵行事項之辦法，由內政部定之。 第一項第五款所定我國基本語言能力及國民權利義務基本常識，其認定、測試、免試、收費及其他應遵行事項之標準，由內政部定之。 

 第 4 條 
 外國人或無國籍人，現於中華民國領域內有住所，具備前條第一項第二款至第五款要件，於中華民國領域內，每年合計有一百八十三日以上合法居留之事實繼續三年以上，並有下列各款情形之一者，亦得申請歸化： 一、為中華民國國民之配偶，不須符合前條第一項第四款。 二、為中華民國國民配偶，因受家庭暴力離婚且未再婚；或其配偶死亡後未再婚且有事實足認與其亡故配偶之親屬仍有往來，但與其亡故配偶婚姻關係已存續二年以上者，不受與親屬仍有往來之限制。 三、對無行為能力、或限制行為能力之中華民國國籍子女，有扶養事實、行使負擔權利義務或會面交往。 四、父或母現為或曾為中華民國國民。 五、為中華民國國民之養子女。 六、出生於中華民國領域內。 七、為中華民國國民之監護人或輔助人。 未婚且未滿十八歲之外國人或無國籍人，有下列情形之一者，在中華民國領域內合法居留雖未滿三年且未具備前條第一項第二款、第四款及第五款要件，亦得申請歸化： 一、父、母、養父或養母現為中華民國國民。 二、現由社會福利主管機關或社會福利機構監護。 

 第 5 條 
 外國人或無國籍人，現於中華民國領域內有住所，具備第三條第一項第二款至第五款要件，並具有下列各款情形之一者，亦得申請歸化： 一、出生於中華民國領域內，其父或母亦出生於中華民國領域內。 二、曾在中華民國領域內合法居留繼續十年以上。 三、由中央目的事業主管機關推薦之高級專業人才，有助中華民國利益，並經內政部邀請社會公正人士及相關機關共同審核通過，且於中華民國領域內，每年合計有一百八十三日以上合法居留之事實繼續二年以上，或曾在中華民國領域內合法居留繼續五年以上。 前項第三款所定高級專業人才之認定要件、審核程序、方式及其他相關事項之標準，由內政部定之。 

 第 6 條 
 外國人或無國籍人，有殊勳於中華民國者，雖不具備第三條第一項各款要件，亦得申請歸化。 內政部為前項歸化之許可，應經行政院核准。 依第一項規定申請歸化者，免徵國籍許可證書規費。 

 第 7 條 
 歸化人之未婚且未滿十八歲子女，得申請隨同歸化。 

 第 8 條 
 外國人或無國籍人依第三條至第七條申請歸化者，應向內政部為之，並自許可之日起取得中華民國國籍。 

 第 9 條 
 外國人申請歸化，應於許可歸化之日起，或依原屬國法令須滿一定年齡始得喪失原有國籍者自滿一定年齡之日起，一年內提出喪失原有國籍證明。 屆期未提出者，除經外交部查證因原屬國法律或行政程序限制屬實，致使不能於期限內提出喪失國籍證明者，得申請展延時限外，應撤銷其歸化許可。 未依前二項規定提出喪失原有國籍證明前，應不予許可其定居。 外國人符合下列情形之一者，免提出喪失原有國籍證明： 一、依第五條第一項第三款規定申請歸化。 二、依第六條第一項規定申請歸化。 三、因非可歸責於當事人之事由，致無法取得喪失原有國籍證明。 

 第 10 條 
 外國人或無國籍人歸化者，不得擔任下列各款公職： 一、總統、副總統。 二、立法委員。 三、行政院院長、副院長、政務委員；司法院院長、副院長、大法官；考試院院長、副院長、考試委員；監察院院長、副院長、監察委員、審計長。 四、特任、特派之人員。 五、各部政務次長。 六、特命全權大使、特命全權公使。 七、僑務委員會副委員長。 八、其他比照簡任第十三職等以上職務之人員。 九、陸海空軍將官。 十、民選地方公職人員。 前項限制，自歸化日起滿十年後解除之。但其他法律另有規定者，從其規定。 

 第 11 條 
 中華民國國民有下列各款情形之一者，經內政部許可，喪失中華民國國籍： 一、由外國籍父、母、養父或養母行使負擔權利義務或監護之無行為能力人或限制行為能力人，為取得同一國籍且隨同至中華民國領域外生活。 二、為外國人之配偶。 三、依中華民國法律有行為能力，自願取得外國國籍。但受輔助宣告者，應得其輔助人之同意。 依前項規定喪失中華民國國籍者，其未成年子女，經內政部許可，隨同喪失中華民國國籍。 前項未成年子女，於本法中華民國一百零九年十二月二十九日修正之條文施行前結婚，修正施行後未滿十八歲者，於滿十八歲前仍適用修正施行前之規定。 

 第 12 條 
 依前條規定申請喪失國籍者，有下列各款情形之一，內政部不得為喪失國籍之許可： 一、男子年滿十五歲之翌年一月一日起，未免除服兵役義務，尚未服兵役者。但僑居國外國民，在國外出生且於國內無戶籍者或在年滿十五歲當年十二月三十一日以前遷出國外者，不在此限。 二、現役軍人。 三、現任中華民國公職者。 

 第 13 條 
 有下列各款情形之一者，雖合於第十一條之規定，仍不喪失國籍： 一、為偵查或審判中之刑事被告。 二、受有期徒刑以上刑之宣告，尚未執行完畢者。 三、為民事被告。 四、受強制執行，未終結者。 五、受破產之宣告，未復權者。 六、有滯納租稅或受租稅處分罰鍰未繳清者。 

 第 14 條 
 依第十一條規定喪失中華民國國籍者，未取得外國國籍時，得經內政部之許可，撤銷其國籍之喪失。 

 第 15 條 
 依第十一條規定喪失中華民國國籍者，現於中華民國領域內有住所，並具備第三條第一項第三款、第四款要件，得申請回復中華民國國籍。 歸化人及隨同歸化之子女喪失國籍者，不適用前項規定。 

 第 16 條 
 回復中華民國國籍者之未成年子女，得申請隨同回復中華民國國籍。 

 第 17 條 
 依第十五條及第十六條申請回復中華民國國籍者，應向內政部為之，並自許可之日起回復中華民國國籍。 

 第 18 條 
 回復中華民國國籍者，自回復國籍日起三年內，不得任第十條第一項各款公職。但其他法律另有規定者，從其規定。 

 第 19 條 
 歸化、喪失或回復中華民國國籍後，除依第九條第一項規定應撤銷其歸化許可外，內政部知有與本法之規定不合情形之日起二年得予撤銷。但自歸化、喪失或回復中華民國國籍之日起逾五年，不得撤銷。 經法院確定判決認其係通謀為虛偽結婚或收養而歸化取得中華民國國籍者，不受前項撤銷權行使期間之限制。 撤銷歸化、喪失或回復國籍處分前，內政部應召開審查會，並給予當事人陳述意見之機會。但有下列情形之一者，撤銷其歸化許可，不在此限： 一、依第二條規定認定具有中華民國國籍。 二、經法院確定判決，係通謀為虛偽結婚或收養而歸化取得中華民國國籍。 前項審查會由內政部遴聘有關機關代表、社會公正人士及學者專家共同組成，其中任一性別不得少於三分之一，且社會公正人士及學者專家之人數不得少於二分之一。 第三項審查會之組成、審查要件、程序等事宜，由內政部定之。 

 第 20 條 
 中華民國國民取得外國國籍者，不得擔任中華民國公職；其已擔任者，除立法委員由立法院；直轄市、縣（市）、直轄市山地原住民區、鄉（鎮、市）民選公職人員，分別由行政院、內政部、直轄市政府、縣政府；村（里）長由鄉（鎮、市、區）公所解除其公職外，由各該機關免除其公職。但下列各款經該管主管機關核准者，不在此限： 一、公立大學校長、公立各級學校教師兼任行政主管人員與研究機關（構）首長、副首長、研究人員（含兼任學術研究主管人員）及經各級主管教育行政或文化機關核准設立之社會教育或文化機構首長、副首長、聘任之專業人員（含兼任主管人員）。 二、公營事業中對經營政策負有主要決策責任以外之人員。 三、各機關專司技術研究設計工作而以契約定期聘用之非主管職務。 四、僑務主管機關依組織法遴聘僅供諮詢之無給職委員。 五、其他法律另有規定者。 前項第一款至第三款人員，以具有專長或特殊技能而在我國不易覓得之人才且不涉及國家機密之職務者為限。 第一項之公職，不包括公立各級學校未兼任行政主管之教師、講座、研究人員、專業技術人員。 中華民國國民兼具外國國籍者，擬任本條所定應受國籍限制之公職時，應於就（到）職前辦理放棄外國國籍，並於就（到）職之日起一年內，完成喪失該國國籍及取得證明文件。但其他法律另有規定者，從其規定。 

 第 21 條 
 （刪除） 

 第 22 條 
 本法施行細則由內政部定之。 

 第 23 條 
 本法自公布日施行。 本法中華民國一百零九年十二月二十九日修正之條文，自一百十二年一月一日施行。 

 ::: 

 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 綜合查詢 
 跨機關檢索 

 法治宣導專區

 智慧查找 
 法律扶助 
 創意教案 

 法律時事漫談 

 網站使用說明

 網站使用手冊 
 會員服務介紹 
 網站單元簡介 
 法規資料檢索範圍 
 資料更新頻率說明 

 資訊服務

 全國法規連結圖示 
 全國法規作業要點 
 法規名稱英譯標準表 

 相關網站 

 訂閱電子報 

 瀏覽人次總計 
 1,529,824,275人 

 本月瀏覽人次 
 5,288,393人 

 目前使用人次 
 32人 

 電子報訂閱人數 
 221,218人 

 本網站係提供法規之最新動態資訊及資料檢索，並不提供法規及法律諮詢之服務。 
 若有任何法律上的疑義，建議您可逕向發布法規之主管機關洽詢。 
 本網站法規資料係由政府各機關提供之電子檔或書面文字登打製作，若與各法規主管機關之公布文字有所不同，仍以各法規主管機關之公布資料為準。 
 部分資料內容，使用特殊文字或符號，如欲詳閱內容，請連結至 司法院網站 下載造字檔。 
 全國法規資料庫之內容每週五定期更新，當週發布之法律、命令資料，將於完成法規整編作業後，於下週五更新上線。 
 法規整編資料截止日：民國 115 年 01 月 09 日 
 瀏覽人次總計：1,529,824,275人 
 本月瀏覽人次：5,288,393人 
 目前使用人次：32人 
 電子報訂閱：221,218人 

 │ 政府網站資料開放宣告 │ 隱私權保護宣告 │ 資訊安全政策 │ Q & A │ 意見回饋 │ API文件 │ 
 本網站由法務部全國法規資料庫工作小組維運管理.. 
 法務部地址：100204 台北市重慶南路一段130號 　 電話：(02)2191-0189 
 第二辦公室地址：100006 台北市貴陽街1段235號 　 電話：(02)2191-0189 

 回上方 

 $(function () {
 var b = 'ONEBAR';
 $("#btnSubscribe,#btnUnsubscribe").on("click", function (event) {
 //var email = $.trim($("#txtEMail").val());
 //if (email == "") {
 // event.preventDefault();
 // alert('請您輸入電子郵件地址。');
 // $("#txtEMail").focus();
 //}
 //else if (false == IsEMail(email)) {
 // event.preventDefault();
 // alert('請您輸入正確電子郵件地址。');
 // $("#txtEMail").focus();
 //}
 //else {
 // GoogleAnanlytice('中文', '訂閱電子報', '', '');
 //}
 var email = $.trim($("#txtEMail").val());
 //if (!validateEmail(email)) {
 // alert('請您輸入正確電子郵件地址。');
 // return false;
 //}

 });
 $('#btnQall').on("click", function () {
 if ($.trim($("#keyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnDeepSearch').on("click", function () {
 var keyword = '';

 //20210315 加上判斷，取QueryString(KW)，若輸入關鍵字已搜尋過，則跳出提示訊息，避免重複搜尋
 Request = GetRequest();
 if ($.trim($("#keyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 }
 else if (keyword.indexOf($.trim($("#keyword").val())) >= 0) {
 alert("此關鍵字已包含至檢索字詞中，請重新輸入");
 return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnMsQall').on("click", function () {
 if ($.trim($("#msKeyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 } else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnMsDeepSearch').on("click", function () {
 var keyword = '';

 //20210315 加上判斷，取QueryString(KW)，若輸入關鍵字已搜尋過，則跳出提示訊息，避免重複搜尋
 Request = GetRequest();
 if ($.trim($("#msKeyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 } else if (keyword.indexOf($.trim($("#msKeyword").val())) >= 0) {
 alert("此關鍵字已包含至檢索字詞中，請重新輸入");
 return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 //20210217 再檢索收合、展開功能
 $("#btnOpen").click(function () {
 if ($('#ulDeepSearch').css('overflow') == 'hidden') {
 $(this).html("收合");
 $(this).prop('title', '隱藏部分「再檢索」篩選條件，僅顯示一行');
 $("#ulDeepSearch").css("overflow", "inherit");
 }
 else {
 $(this).html("展開");
 $(this).prop('title', '顯示所有目前「再檢索」篩選條件');
 $("#ulDeepSearch").css("overflow", "hidden");
 }
 });
 $("#btnHelp").click(function () {
 OpenKeyWordHelp();
 return false;
 });
 $('#dropdownMenu').attr('data-bs-toggle', 'dropdown');
 $('#unitlist').on("click", "a", function (e) {
 e.preventDefault();
 var $this = $(this).parent();
 var a = $(this).html();
 b = $this.data("value");
 $this.addClass("select").siblings().removeClass("select");
 $("#dropdownMenu").html(a);
 $('#hidVal').val(b);
 });
 //$('#keyword').on('input propertychange paste keypress', function () {
 // BindAutocomplete('#keyword', b);
 //});
 BindAutocompletes('#keyword', b);
 function BindAutocompletes(orl, stype) {

 $(orl).autocomplete({
 source: function (request, response) {
 $.ajax({
 url: "../controls/GetTermList.ashx",
 type: 'post',
 dataType: "json",
 data: {
 term: request.term, type: stype
 },
 success: function (data) {
 response(data);
 }
 });
 },
 minLength: 1, //至少輸入幾個字元才開始給提示
 focus: function (event, ui) {
 return false;
 },
 select: function (event, ui) {
 if ($.trim(ui.item.PCODE).length == 0)
 $(this).val(ui.item.TERM);
 else
 location.href = "../Hot/AddHotLaw.ashx?pcode=" + encodeURIComponent(ui.item.PCODE);

 return false;
 },
 messages: { noResults: '', results: function () { } }//不顯示結果文字
 }).data("ui-autocomplete")._renderItem = function (ul, item) {
 if ($.trim(item.PCODE) != "")
 return $(" ")
 .append(" 直接連結 " + item.TERM + " ")
 .appendTo(ul);
 else {
 if (ul.find(".label-usual").length == 0)
 return $(" ")
 .append(" 常用詞彙 " + item.TERM + " ")
 .appendTo(ul);
 else
 return $(" ")
 .append(" " + item.TERM + " ")
 .appendTo(ul);
 }
 };
 }
 });
 function validateEmail(email) {
 if (email.includes("%")) {
 return false;
 }
 return true;
 }
 function OpenKeyWordHelp() {
 var a = "/Service/KeyWordHelp.html";
 TINY.box.show({ iframe: a, width: 810, height: 680 });
 //return false;
 }
 function GetRequest() {
 var url = location.search;
 var theRequest = new Object();
 if (url.indexOf("?") != -1) {
 var str = url.substr(1);
 strs = str.split("&");
 for (var i = 0; i 1200) {
 var Request = new Object();
 Request = GetRequest();
 var keyword = '';
 if (keyword != null && keyword.length > 26) {
 var ui = document.getElementById("btnOpen");
 ui.style.display = "";
 }
 } else {
 var Request = new Object();
 Request = GetRequest();
 var keyword = '';
 if (keyword != null && keyword.length > 19) {
 var ui = document.getElementById("btnOpen");
 ui.style.display = "";
 }
 }

 $(function () {
 $('[data-fancybox]').fancybox({
 toolbar: false,
 smallBtn: true,
 iframe: {
 css: {
 width: '400px',
 height: '170px'
 }
 }
 });
 });

//
