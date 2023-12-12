<p align="center" width="100%">
     <img width="99%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/eb619d22-7723-41df-ac65-69c98bda1a64">
     </p>
     

# ⚔ LoL Win-Loss Prediction 🏆
<b>리그 오브 레전드(LoL)</b> 게임 데이터를 활용한 승패 예측 모델 개발


## 1. 개 요


<h5><p align="center" width="100%">
     <img width="45%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/9783dd92-ef52-4a33-b449-8002894144b6">
     <img width="54%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/dc9b0604-e098-4fa7-9936-978a5e09f20f"> <br>
     (좌: 23년 11월 PC방 주간 점유율 순위) /   
     (우: 중국 제외 37개국 PC게임 MAU 통계)</h5></p>


   * ### 문제정의
     "League of Legends(이하 LoL)"는 Riot Games에서 개발한 인기 있는 온라인 게임으로, 전 세계적으로 많은 플레이어들이 즐기고 있다.
     이 게임은 전략과 팀워크가 필요한 멀티플레이어 배틀 아레나(MOBA) 장르의 게임이며, e-sports 산업에서 주목받는 콘텐츠로 자리매김하고 있다.
     2022년 항저우 아시안 게임에서는 LoL이 정식 종목으로 채택되는 등 LoL은 이미 성과와 영향력이 검증되었다는 것을 알 수 있다.

     Riot Games는 투명성 확보를 위해 다양한 게임 데이터를 무료로 제공하고 있다. 소환사 정보, 챔피언 정보, 게임 정보, 랭킹 및 리그 정보 등의 게임 데이터는 Riot Games의 API를 통해 접근 가능하다. 이와 같이 제공되는 데이터는 통계적 분석에 활용할 수 있으며, 하루에 약 20만 건의 다양한 게임 데이터가 수집된다. 이렇게 쉽게 접근 가능한 데이터를 활용하면, 깊이 있는 분석과 예측 모델 구축이 가능해진다.

     이번 프로젝트에서는 Riot Games API에서 제공하는 데이터를 활용하여, LoL 게임의 승패를 예측하는 모델을 개발하고자 한다. 이 모델은 플레이어의 게임 데이터를 입력으로 받아, 해당 게임의 승패를 예측한다. 이를 통해 플레이어는 자신의 게임 전략을 개선하는 데 도움을 받을 수 있으며, 승률 향상에 기여할 수 있다. 또한 이 모델은 LoL 게임의 승패 패턴을 이해하고 그 내재된 메커니즘을 파악하는 데에도 도움이 될 것으로 기대된다.

<hr>


## 2. 데이터

   ### 2.1 데이터 소스
이번 프로젝트에 활용할 데이터는 온라인 게임 코칭 전문기업인 더매치랩(The Match LAB)에서 가공한 LoL 게임 데이터를 바탕으로 한다. 
데이터는 2023년 8월 25일, 9월 15일, 9월 17일 각각 하루 동안 수집된 LoL 경기에 대한 세부 항목들로 구성되어 있다.

   ### 2.2 탐색적 데이터 분석
데이터는 5대5 솔로 랭크 경기 약 20만 건으로 구성되어 있으며, 포지션별로 데이터가 구분되어 있다. 
5가지 포지션에 대한 내용은 다음과 같다.

* LOL 게임에 대한 간략한 설명
* 영상 삽입

     <p align="center" width="100%">
     <img width="60%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/31b7d9a9-6a93-48e9-a7c6-d43f8c576936">
     </p>

  

| 포지션    |역할|
|--------|---|
| 탑(TOP) | 탑 라이너는 게임 맵의 상단에 위치하며, 주로 챔피언 간의 1대1 싸움에 특화되어 있다. 강인한 챔피언들이나 방어적인 챔피언들이 탑 라인에서 주로 플레이한다. |
| 정글(JUNGLE) | 정글러는 맵의 숲 지역을 돌아다니며 몬스터를 처치하고 팀원들을 지원한다. 또한 적군 정글러와의 교전에서 승리를 가져오는 역할을 한다. 정글러는 각 라인을 돕고 중요한 중립 몬스터들을 처치하여 경험치와 골드를 얻는다. |
| 미드(MID) | 미드 라이너는 맵의 중앙에 위치하며, 적과 아군 간의 중요한 교전이 일어나는 지점이다. 미드 라이너는 게임의 중반에 팀에 큰 영향을 미칠 수 있는 중요한 역할을 맡는다. |
| 원딜(AD Carry) | 원딜러는 주로 하프맵의 아래에 위치한 라인에서 플레이한다. 고사거나 원거리 공격력이 높은 챔피언으로, 게임의 후반에 팀에게 높은 데미지를 제공하는 역할을 한다. |
| 서포트(SUPPORT) | 서포터는 주로 원딜러와 함께 아래 라인에서 플레이하며, 팀원들을 지원하고 적에게 방해를 주는 역할을 한다. 힐링, 감속, CC(제어) 스킬 등을 통해 팀의 생존력을 높이고 원딜러에게 안전한 플레이를 가능하게 한다. |

제공된 데이터의 항목은 총 185개로 구성되어 있으며, 전반적으로 다음과 같은 내용으로 정리해 볼 수 있다.

| 항목             | 데이터 속성 |
|----------------|--------|
| 플레이어에 대한 데이터   | ???    |
| 팀에 대한 데이터      | ???    |
| 라인전 전후에 대한 데이터 |???|

여기서 중요하게 고려되는 항목들은 다음과 같다. (10개 이상)

| 데이터 속성 | 데이터의 의미     | 중요한 이유 |
|-------|-------------|--------|
| KDA   | Kill/Death/Assist의 비율 |
| 팀에 대한 데이터 | ???         |
| 라인전 전후에대한 데이터 | ???         |

   ### 2.3 데이터 전처리
20만 건의 경기 데이터는 수준 별로 편차가 어느정도 존재할 것으로 예상된다. 
따라서 일정 수준 이상의 데이터로 지표의 상관성을 통해 승패예측 모델을 만드는 것이 합리적일 것이다.

이에 이번 프로젝트에서는 다음과 같이 정의되는 LoL게임의 등급체계(tier)를 바탕으로, 모든 플레이어가 플래티넘 이상인 경기를 추출하여 분석해보고자 한다.

* 티어에 대한 정보 (표)
* 티어별 히스토그램
* 플래티넘 이상인 경기의 수

도출된 플래티넘 이상의 경기에 대해서, 핵심 데이터 속성으로 ???, ???, ??? 등을 추출했다. 
그 이유는 ~~~때문이다. 
그리고 승패를 예측하는 것이기 때문에, 경기 데이터를 기준으로 데이터 속성별 정규화(normalize)를 수행했다. 

   ### 2.4 데이터 프레임 설계
탐색적 데이터 분석과 데이터 전처리를 통해 다음과 같은 데이터 프레임을 만들고자 한다.

| Id  | 팀  | 주요지표 | TOP |MID|
|-----|-----|---------|-----|---|
| 고유번호 | Red/Blue | kda, dpd, ...| ... |...|
<hr>

## 3. 승패예측 모델

   ### 3.1 모델 개요
   CNN을 썼다. 단순한 합산을 썼다.

## 3.2 성능
0825 <br>
0915 <br>
0917 <br>
플래티넘 이상 4.5만건
데이터 전체 20만건

   ### 3.3 소결
* 성능에 대한 의미
* 핵심 데이터 항목에 대한 추정 및 분석
<hr>

## 4. 결론 및 배운점


<hr>
       
       
   ## References
   [01] https://www.thelog.co.kr/report/reportView.do?nSeq=265 <br>
   [02] https://pgr21.com/free2/72613 <br>

   




