<p align="center" width="100%">
     <img width="99%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/eb619d22-7723-41df-ac65-69c98bda1a64">
     </p>
     

# ⚔ LoL Win-Loss Prediction 🏆
### <b>리그 오브 레전드(LoL)</b> 게임 데이터를 활용한 승패 예측 모델 개발


# 1. 개 요
     
"League of Legends(이하 LoL)"는 Riot Games에서 개발한 인기 있는 온라인 게임으로, 전 세계적으로 많은 플레이어들이 즐기고 있다.
이 게임은 전략과 팀워크가 중요한 멀티플레이어 배틀 아레나(MOBA) 장르의 게임이며, e-sports 산업에서 주목받고 있다<sup>[[01]](https://weekly.chosun.com/news/articleView.html?idxno=30406)</sup>. 

<h5><p align="center" width="100%">
     <img width="45%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/9783dd92-ef52-4a33-b449-8002894144b6">
     <img width="54%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/dc9b0604-e098-4fa7-9936-978a5e09f20f"> <br>
     ( 좌: <a href="https://www.thelog.co.kr/report/reportView.do?nSeq=265">23년 11월 PC방 주간 점유율 순위</a> ) /   
     ( 우: <a href="https://pgr21.com/free2/72613">중국 제외 37개국 PC게임 MAU 통계</a> )</p></h5>

PC방 게임 통계서비스에 의하면 LoL은 2018년 8월부터 5년 넘게 PC방 주간 점유율 순위에서 꾸준히 1위를 차지하고 있으며<sup>[[02]](https://www.thelog.co.kr/report/reportView.do?nSeq=265)</sup>, 중국을 제외한 37개국의 PC게임 MAU 통계에서도 1위를 차지하는 등<sup>[[03]](https://www.thelog.co.kr/report/reportView.do?nSeq=265)</sup> LoL의 영향력은 매우 큰 것을 알 수 있다. 
또한, 2022년 항저우 아시안 게임에서 정식 종목으로 채택되면서 그만큼 높은 성과를 보이고 있다.

Riot Games는 게임 자체의 재미뿐만 아니라 분석 가능한 다양한 게임 데이터를 무료로 제공하고 있다. 소환사 정보, 챔피언 정보, 게임 정보, 랭킹 및 리그 정보 등의 게임 데이터는 Riot Games의 API를 통해 접근할 수 있다. 데이터는 하루에 약 20만 건의 게임 데이터가 수집되며, 소정의 절차를 거쳐 쉽게 접근 할 수 있다. 해당 데이터를 통해 게임에 대한 통계적 분석과 예측 모델을 구축할 수 있다.

이번 프로젝트에서는 Riot Games API에서 제공하는 데이터를 활용하여, LoL 게임의 승패를 예측하는 모델을 개발하고자 한다. 이 모델은 플레이어의 게임 데이터를 입력으로 받아, 게임의 다양한 요소와 플레이어의 행동 패턴 등을 분석하여 해당 게임의 승패를 예측한다. 이를 통해 플레이어는 자신의 게임 전략을 개선하는 데 도움을 받을 수 있으며, 승률 향상에 기여할 수 있다.
<!-- 또한 이 모델은 LoL 게임의 승패 패턴을 이해하고 그 내재된 메커니즘을 파악하는 데에도 도움이 될 것으로 기대된다. -->

<hr>


# 2. 데이터

## 2.1 데이터 소스
이번 프로젝트에 활용할 데이터는 온라인 게임 코칭 전문기업인 더매치랩(The Match LAB)에서 가공한 LoL 게임 데이터를 바탕으로 한다. 
데이터는 2023년 8월 25일, 9월 15일, 9월 17일 각각 하루 동안 수집된 LoL 경기에 대한 세부 항목들로 구성되어 있다.

## 2.2 탐색적 데이터 분석

<!-- * LOL 게임에 대한 간략한 설명 -->
LoL은 5명의 팀원으로 이루어진 두 팀이 서로 대립하여 상대편의 기지를 파괴하기 위해 치열한 사투를 벌이는 전략 게임이다. 
이 게임에서는 각 플레이어의 역할과 포지션이 나눠지며, 이에 따른 다양한 전략과 팀워크가 중요한 요소로 작용한다. 게임의 주요 흐름은 아래와 같다.

<b>[ 시작 및 포지셔닝 ]</b>
  - 게임이 시작되면 5명의 팀원은 사전에 합의한 Top, Jungle, Mid, Bottom(ADC, SPT) 라인으로 흩어진다. 각 포지션은 고유한 역할을 가지고 있으며, 이를 잘 수행하는 것이 중요하다.
    
<b>[ 라인전 진행 ]</b>
- 각 라인에서는 상대편의 포탑을 철거하고, 아군의 포탑을 지키기 위해 상대편과 대치한다. 이 과정에서 적의 챔피언이나, 미니언을 처치하여 골드와 경험치를 얻는다.
  
<b>[ 포탑 파괴 ]</b>
-  상대편의 포탑을 파괴하면 아군의 공격로가 확장되며, 적의 기지를 향해 나아갈 수 있게 된다. 포탑을 파괴하는 것은 게임을 유리하게 진행시키는 중요한 부분이다.
  
<b>[ 넥서스(기지)를 파괴하여 승리 ]</b>
- 넥서스로 향한 길목에 위치한 포탑들을 모두 파괴하고, 마지막으로 상대편의 넥서스를 파괴하면 승리하게 된다.

---

<h4><p align="center" width="100%">
     <img width="70%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/3d87df29-d37f-4c16-be4b-a94b1438c8d5"><br>
     ( LoL에 등장하는 맵 - 소환사의 협곡 )
     </p></h4>


소환사의 협곡은 LoL의 가장 대표적인 맵으로, 플레이어들이 대결하고 경쟁하는 공간이다. <br>
맵은 기본적으로 TOP, MID, BOTTOM 3개의 라인으로 나뉘고, 맵의 중앙에는 정글이 위치하고 있다. 각 위치별로 포지션이 정해져 있으며, 포지션은 탑(TOP), 정글(JUG), 미드(MID), 원딜(ADC), 서폿(SPT) 총 5가지로 구분된다. 

포지션에 대한 자세한 내용은 다음과 같다.


| 포지션 | 위치  |역할|
|:--------:|:---:|-----|
| 탑<br>(TOP) |   상단 라인   | 탑 라이너는 게임 맵의 상단에 위치하며, 주로 챔피언 간의 1대1 싸움에 특화되어 있다. 강인한 챔피언들이나 방어적인 챔피언들이 탑 라인에서 주로 플레이한다. |
| 정글<br>(JUG) |  정글 지역, 전체 라인  | 정글러는 맵의 정글 지역을 돌아다니며 몬스터를 처치하고 팀원들을 지원한다. 또한 적군 정글러와의 교전에서 승리를 가져오는 역할을 한다. 정글러는 각 라인을 돕고 중요한 몬스터들을 처치하여 경험치와 골드를 얻는다. |
| 미드<br>(MID) |  중앙 라인  | 미드 라이너는 맵의 중앙에 위치하며, 적과 아군 간의 중요한 교전이 일어나는 지점이다. 미드 라이너는 게임의 중반에 팀에 큰 영향을 미칠 수 있는 중요한 역할을 맡는다. |
| 원딜<br>(ADC) |  하단 라인<br>( BOTTOM )  | 원딜러는 주로 맵의 하단 라인에서 플레이한다. 고정 사거리나 원거리 공격력이 높은 챔피언이 주로 플레이하며, 게임의 후반에 팀에게 높은 데미지를 제공하는 역할을 한다. |
| 서폿<br>(SPT) |  하단 라인<br>( BOTTOM )   | 서포터는 주로 원딜러와 함께 하단 라인에서 플레이하며, 팀원들을 지원하고 적에게 방해를 주는 역할을 한다. 힐링, 감속, CC(제어) 스킬 등을 통해 팀의 생존력을 높이고 원딜러에게 안전한 플레이를 가능하게 한다. |

---

데이터는 5대5 솔로 랭크 경기 약 20만 건으로 구성되어 있으며, 3일치의 데이터는 포지션별로 구분되어 있다. <br>
제공된 데이터의 항목은 총 185개로 구성되어 있으며, 전반적으로 다음과 같은 내용으로 정리해 볼 수 있다.

|id|ver|tier|...|dragon200|goldearned100|...|first_dragon_time|first_turret_time|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|고유번호|13016|P|...|4|72259|...|1642|1193|


| 항목             | 데이터 속성 |
|:----------------:|--------|
| 플레이어에 대한 데이터   |tier, cid, assists, cs, kills, deaths ...|
| 팀에 대한 데이터      | dragon, baron, goldearned, turretkills ... |
| 라인전 전후에 대한 데이터 | dpd_at14, gold_af14, kda_at14, solodill_af14 ... |<br>


여기서 중요하게 고려되는 항목들은 다음과 같다.

| 데이터 속성 | 데이터의 의미 | 중요한 이유 |
|:-------------:|:--------------:|-------------|
| win | 승패 여부 | 해당 데이터는 게임의 최종 결과를 나타내며, 이는 우리가 예측하려는 대상이다. 이 데이터는 모델의 성능을 평가하는 데 사용되며, 이번 프로젝트의 최종 목표인 승패 예측에 있어 가장 중요한 데이터다. 모델이 이 데이터를 정확하게 예측하는 것이 이번 프로젝트의 완성도를 결정짓게 된다. |
| kda | (킬 수 + 어시 수) / 데스 수 | 플레이어의 전투 참여와 생존 능력을 종합적으로 평가하는 지표다. 킬(kill)은 플레이어가 적을 처치한 횟수, 데스(death)는 플레이어가 죽은 횟수, 어시스트(assist)는 플레이어가 적 처치에 도움을 준 횟수를 의미한다. 'kda'가 높을수록 플레이어의 전투 참여도가 높고, 생존 능력이 우수함을 의미하므로, 전체 게임에서의 성과에 큰 영향을 미친다. |
| goldearned | 총 획득 골드 | 골드는 게임에서 아이템을 구매하여 챔피언의 능력을 향상시키는 데 시용되므로, 획득 골드량은 플레이어의 성장 속도와 전투력을 나타내는 중요한 지표다. |
| dealt | 챔피언에게 넣은 데미지 | 플레이어가 얼마나 많은 데미지를 적에게 가했는지를 나타낸다. 이는 플레이어의 공격력을 나타내며, 적 챔피언을 제거하거나 전투에서 우위를 점하는데 중요한 지표다. |
| dpd | 데스 당 가한 데미지 | 플레이어가 죽는 횟수 당 얼마나 많은 데미지를 적에게 가했는지를 나타내는 지표다. 이는 플레이어의 공격 효율성을 나타낸다. 'dpd'가 높을수록 플레이어가 적에게 더 많은 피해를 줄 수 있음을 의미하므로, 게임에서의 우위를 점하는데 중요한 역할을 한다. |
| baron | 아군 바론 처치 수 | 바론을 처치하면 팀 전체에게 골드와 경험치를 제공하며, 일정 시간 동안 팀 전체의 공격력이 증가하는 등의 보너스를 부여한다. 이는 게임의 전환점이 될 수 있으므로 중요한 지표다. |
| dragon | 아군 드래곤 처치 수 | 드래곤을 처치하면 팀 전체에게 골드와 경험치를 제공하며, 종류에 따라 다양한 보너스를 부여한다. 드래곤의 종류에 따라 공격력, 방어력, 이동 속도 등 다양한 상승 효과가 있어 게임의 승패에 큰 영향을 준다. |
| turretKills | 포탑 길 수 (막타) | 포탑을 파괴하면 골드와 맵 컨트롤 우위를 얻을 수 있으므로 중요한 전략적 목표이다. 포탑을 파괴함으로써 적진에 더 깊게 진입할 수 있는 길을 열어주며, 게임의 승리에 큰 기여를 한다. |
| dpm | 분 당 가한 데미지 | 게임 시간당 플레이어가 적에게 가한 데미지를 나타내는 지표다. 이는 플레이어의 지속적인 공격력을 평가하는 데 사용되며, 높은 'dpm'은 플레이어가 게임 내내 적에게 지속적으로 높은 피해를 가하고 있음을 의미한다. 이는 전반적인 성과와 게임의 승리에 큰 영향을 미친다. |
| visionscore | 시야 점수 | 시야 점수는 맵의 정보를 획득하고 적의 움직임을 예측하는데 중요하며, 팀 전체의 맵 컨트롤 능력을 나타낸다. 안정적인 판단과 전략을 세우기 위해서는 충분한 정보가 필요하며, 이를 위해 시야 확보는 필수적이다. |
| wardskilled | 와드 파괴 개수 | 와드를 파괴하면 적 팀의 시야를 제거하고, 우리 팀의 안전성과 맵 컨트롤을 높일 수 있다. 시야는 정보를 제공하므로, 적의 와드를 파괴하고 그들의 시야를 제거하는 것은 게임의 승패에 중요한 영향을 미친다. |
| dpg | 골드 당 가한 데미지 | 플레이어가 사용한 골드 당 얼마나 효율적으로 데미지를 가했는지를 나타내는 지표다. 골드를 효율적으로 사용하여 더 많은 데미지를 가하는 것은 게임의 승리에 크게 기여하므로, 이 지표는 매우 중요하다. |

---

## 2.3 데이터 전처리
20만 건의 경기 데이터는 수준 별로 편차가 어느정도 존재할 것으로 예상된다. 
따라서 일정 수준 이상의 데이터로 지표의 상관성을 통해 승패예측 모델을 만드는 것이 합리적일 것이다.

이에 이번 프로젝트에서는 다음과 같이 정의되는 LoL게임의 등급체계(tier)를 바탕으로, 모든 플레이어가 <b>'플래티넘 이상'</b>인 경기를 추출하여 분석해보고자 한다.

### [ 티어에 대한 정보 ] 
LoL의 티어 시스템은 플레이어의 스킬 수준을 평가하고 등급화하는 척도이다. 총 10개의 레벨로 이루어져 있으며, 상위 티어 3개를 제외한 각 티어는 I, II, III, IV의 4개 division으로 세분화된다.

플레이어는 매치 승리로 LP(League Points)를 획득하며, 일정 LP를 얻으면 다음 division 또는 티어로 승급하게 된다. 반대로 패배 시 LP가 감소하고, 연속 패배는 division 또는 티어가 하락하게 된다.

티어 시스템은 플레이어의 실력을 지속적으로 측정하고 업데이트하며, 매치메이킹 시스템에서 비슷한 실력의 플레이어들을 매칭하는 기준으로도 사용된다.

다음은 티어 분포에 대한 시각화 자료이다.


<details>
<summary>한국 티어 분포표 <a href="https://www.op.gg/statistics/tiers"><sup>[출처 : op.gg]</sup></a></summary><br>
<div align="center" width="100%"><img width="80%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/08728fef-4755-4d75-8489-5997553eb691"> </div>

<table align="center">
  <tr align="center"><th colspan="4">내림차순</th><th rowspan="17">　　<th>티어</th><th>단계</th><th>분포</th><th>합</th></tr>
  <tr align="center"><th>티어</th><th>단계</th><th>분포</th><th>합</th><th rowspan="4">골드 G</th><td>Ⅰ</td><td>2.68%</td><td rowspan="4">19.26%</td></tr>
  <tr align="center"><th>챌린저 C</th><td>Ⅰ</td><td>0.01%</td><td>0.01%</td><td>Ⅱ</td><td>3.92%</td></tr>
  <tr align="center"><th>그랜드마스터 R</th><td>Ⅰ</td><td>0.02%</td><td>0.02%</td><td>Ⅲ</td><td>4.85%</td></tr>
  <tr align="center"><th>마스터 M</th><td>Ⅰ</td><td>0.47%</td><td>0.47%</td><td>Ⅳ</td><td>7.81%</td></tr>
  <tr align="center"><th rowspan="4">다이아 D</th><td>Ⅰ</td><td>0.39%</td><td rowspan="4">3.45%</td><th rowspan="4">실버 S</th><td>Ⅰ</td><td>2.78%</td><td rowspan="4">19.04%</td>
  </tr>
  <tr align="center"><td>Ⅱ</td><td>0.55%</td><td>Ⅱ</td><td>4.01%</td></tr>
  <tr align="center"><td>Ⅲ</td><td>0.69%</td><td>Ⅲ</td><td>4.87%</td></tr>
  <tr align="center"><td>Ⅳ</td><td>1.82%</td><td>Ⅳ</td><td>7.38%</td></tr>
  <tr align="center"><th rowspan="4">에메랄드 E</th><td>Ⅰ</td><td>1.59%</td><td rowspan="4">13.68%</td><th rowspan="4">브론즈 B</th><td>Ⅰ</td><td>3.3%</td><td rowspan="4">19.93%</td></tr>
<tr align="center"><td>Ⅱ</td><td>1.93%</td><td>Ⅱ</td><td>4.5%</td></tr>
  <tr align="center"><td>Ⅲ</td><td>3.21%</td><td>Ⅲ</td><td>5.08%</td></tr>
  <tr align="center"><td>Ⅳ</td><td>6.95%</td><td>Ⅳ</td><td>7.05%</td></tr>
  <tr align="center"><th rowspan="4">플래티넘 P</th><td>Ⅰ</td><td>2.15%</td><td rowspan="4">16.97%</td><th rowspan="4">아이언 I</th><td>Ⅰ</td><td>3.11%</td><td rowspan="4">7.21%</td></tr>
  <tr align="center"><td>Ⅱ</td><td>3.22%</td><td>Ⅱ</td><td>2.54%</td></tr>
  <tr align="center"><td>Ⅲ</td><td>4.21%</td><td>Ⅲ</td><td>1.08%</td></tr>
  <tr align="center"><td>Ⅳ</td><td>7.39%</td><td>Ⅳ</td><td>0.48%</td></tr>
</table>
</details>


<details>
<summary>0825 전체 게임 데이터 티어별 분포표</summary><br>
<div align="center" width="100%"><img width="70%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/7a78f08d-3855-443b-a1b8-c62cf2c382e7"> </div>
</details>

<details>
<summary>0915 전체 게임 데이터 티어별 분포표</summary><br>
<div align="center" width="100%"><img width="70%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/73e4a96a-88eb-48e7-b636-43b5c32cef42"> </div>
</details>

<details>
<summary>0917 전체 게임 데이터 티어별 분포표</summary><br>
<div align="center" width="100%"><img width="70%" src="https://github.com/wnaely/LOL_EDA/assets/130523834/b021a633-53d7-4798-a427-41d0b96e32c1"> </div>
</details>

전체 게임 데이터의 티어별 분포를 살펴보면 '브론즈'부터 '에메랄드' 티어의 플레이어 데이터가 가장 많다. 반면, 챌린저와 그랜드마스터 티어의 플레이어 데이터 수는 상대적으로 매우 적은 것을 확인할 수 있는데, 아는 실제 게임의 티어 분포와 비슷하게 나타난다.

---
  
### [ 플래티넘 이상인 경기의 수 ]
  
| 데이터 | 0825 | 0915 | 0917 |
|:--:|:----:|:----:|:----:|
| 플래티넘 ↑ | 44962 | 28209 | 25208 |
<br>

플래티넘 티어 이상의 경기 데이터에서 'kda', 'dpd', 'dpm', 'dpg', 'dtpm'를 핵심 데이터로 속성으로 추출했다.
'kda'는 플레이어의 킬, 데스, 어시스트를 종합적으로 고려한 지표로, 플레이어의 전반적인 전투 성과를 나타낸다.
'dpd'는 데스당 입힌 피해량을, 'dpm'은 분당 입힌 피해량을 나타내는 지표로, 플레이어의 공격 효율성을 측정한다.
추출한 핵심 데이터는 모두 전투와 직접적으로 관련되어 있고, 전투 능력과 게임에서의 성과는 게임 승패에 결정적인 영향을 미친다고 생각하기 때문에 해당 데이터를 핵심 데이터로 추출하였다. 

게임 승패에 대한 정확한 예측을 위해 경기 데이터를 기준으로 데이터 속성별 정규화(normalize)를 수행했다. 
각 지표가 다른 스케일을 가지고 있을 수 있으므로, 이를 통일시켜 모델의 학습 과정을 효율적으로 하며, 각 지표가 예측에 과도하게 영향을 미치는 것을 방지한다.

--- 

## 2.4 데이터 프레임 설계
탐색적 데이터 분석과 데이터 전처리를 통해 다음과 같은 데이터 프레임을 만들고자 한다.

<table>
  <tr align="center"><th>Id</th><th>팀</th><th>주요지표</th><th>TOP</th><th>MID</th><th>JUG</th><th>ADC</th><th>SPT</th></tr>
  <tr align="center"><th rowspan="7">고유번호</th><th rowspan="7">100/200<br>( Blue/Red )</th><td>kda</td><td>···</td><td>0.005714</td><td>...</td><td>0.0</td><td>···</td></tr>
  <tr align="center"><td>dpd</td><td>···</td><td>0.0</td><td>...</td><td>0.053588</td><td>···</td></tr>
  <tr align="center"><td>dpm</td><td>···</td><td>0.249978</td><td>...</td><td>0.077396</td><td>···</td></tr>
  <tr align="center"><td>dpg</td><td>···</td><td>0.00542</td><td>··</td><td>0.684343</td><td>···</td></tr>
  <tr align="center"><td>dtpm</td><td>···</td><td>0.335697</td><td>···</td><td>0.091548</td><td>···</td></tr>
  <tr align="center"><td>win</td><td>···</td><td>0</td><td>···</td><td>0</td><td>···</td></tr>
  <tr align="center"><td>tier</td><td>···</td><td>P</td><td>···</td><td>G</td><td>···</td></tr>
</table>

---

# 3. 승패예측 모델

## 3.1 모델 개요
이 프로젝트에서는 단순 합산 방법과 함성곱 신경망(CNN) 두 가지 방법을 사용하였다.

<b>'단순 합산 방법'</b>은 각 경기 데이터에서 플레이어의 주요 지표를 합산하여 승패를 예측하는 방식이다.
이 방식은 각 플레이어의 성과를 단순히 더함으로써, 팀의 전반적인 성과를 쉽게 파악하고 이를 바탕으로 승패를 예측할 수 있다.
이 방법의 장점은 간결함과 직관적인 해석 가능성에 있다. 하지만 각 지표의 상호작용이나 각 플레이어의 개별적인 영향력 등 더 복잡한 요소를 고려하지 않는다는 한계가 있다.

<b>'CNN'</b>은 주어진 데이터에서 복잡한 패턴을 학습하고 이를 바탕으로 승패를 예측하는 방식이다. CNN은 합성곱 계층과 풀링 계층을 통해 원본 데이터에서 중요한 특징들을 추출하고 학습하는 방식으로 동작한다. 이 방법은 복잡한 패턴을 발견하고 이를 통해 더 정확한 예측을 가능하게 하는 것이 장점이다.

## 3.2 LoL 게임 데이터 분석 과정

### [ 단순 합산 ]

``` python
...

position = ['TOP', 'MID', 'JUG', 'SPT', 'ADC']
features = ['kda', 'dpd', 'dpg', 'dpm', 'dtpm']
...
for id in ids:
    blue_data = df.loc[idx[id, 100, features]].values
    blue_data = list(np.concatenate(blue_data))
    red_data  = df.loc[idx[id, 200, features]].values
    red_data  = list(np.concatenate(red_data))
    blue_win = df.loc[idx[id, 100, 'win']].values
    win  = blue_win[0]
    blue_sum = sum(blue_data)
    red_sum = sum(red_data)
    forecast = 0
    if blue_sum > red_sum : forecast = 1
    acc = 0
    if win == forecast: acc =1

...
```
플레이어의 포지션(TOP, MID, JUG, SPT, ADC)과 특징 데이터(kda, dpd, dpg, dpm, dtpm)를 기준으로 블루팀과 레드팀의 데이터를 추출하고, 이를 합산하여 블루팀과 레드팀의 총 점수를 계산한다. 
이후 블루팀의 점수가 레드팀의 점수보다 높은 경우 예측 승리팀을 블루팀으로, 그렇지 않은 경우 레드팀으로 예측한다.

이렇게 예측된 승리팀과 실제 승리팀을 비교하여 예측의 정확도를 계산한다. 이 과정을 각 게임에 대해 반복하며, 각 게임의 예측 정보(ID, 블루팀 데이터, 레드팀 데이터, 승리팀, 예측 승리팀, 예측 정확도)를 저장한다.

마지막으로, 모든 게임에 대한 예측 정확도의 합을 계산하고, 이를 게임 수로 나누어 전체 예측 정확도를 계산한다.
이 결과를 출력하여 모델의 전체 예측 성능을 확인한다.

### [ CNN ]

``` python
...

model = Sequential()
model.add(Conv2D(75, (3,3), strides=1, padding="same", activation="relu", input_shape=(10,5,1)))
model.add(BatchNormalization())
model.add(MaxPool2D((2,2), strides=2, padding="same"))
model.add(Conv2D(50, (3,3), strides=1, padding="same", activation="relu"))
...
model.add(MaxPool2D((2,2), strides=2, padding="same"))
model.add(Flatten())
model.add(Dense(units=265, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(units=num_classes, activation="softmax"))

...
```
데이터를 불러온 후 데이터의 레이블(승패 정보)을 분리하고, 데이터를 CNN 모델에 적합한 형태로 변환한다.
CNN 모델은 여러 개의 Conv2D(합성곱 계층), MaxPool2D(풀링 계층), Dropout(드롭아웃 계층), BatchNormalization(배치 정규화 계층)으로 구성되어 있으며, 이러한 계층들은 순차적(Sequential)으로 배열되어 있다. 

Conv2D는 데이터에서 패턴을 학습하며, MaxPool2D는 데이터의 크기를 줄이는 데 사용된다. Dropout은 과적합을 방지하는 역할을 하며, BatchNormalization은 학습을 안정화하고 가속화하는 데 도움을 준다.

마지막으로, Fltten을 통해 2차원의 특징 맵을 1차원으로 변환하고, 이를 바탕으로 Dense를 통해 분류 작업을 수행한다.
모델 구성 후, 'categorical_crossentropy'를 손실 함수로, 'adam'을 최적화 방법으로, 'accuracy'를 성능 지표로 사용하여 모델을 컴파일하고, fit 함수를 사용하여 모델을 학습시킨다. 이때, 텐서보드를 콜백으로 설정하여 학습 과정을 모니터링한다.

---

## 3.2 성능
<table>
  <tr align="center"><th>데이터</th><th>구분</th><th>정확도(단순)</th><th>정확도(CNN)</th></tr>
  <tr align="center"><th rowspan="2">0825</th><td>플래티넘 ↑</td><td>95%</td><td>95.8%</td></tr>
  <tr align="center"><td>전체</td><td>93.6%</td><td>94.2%</td></tr>
  <tr align="center"><th rowspan="2">0915</th><td>플래티넘 ↑</td><td>93.4%</td><td>94.8%</td></tr>
  <tr align="center"><td>전체</td><td>90.3%</td><td>93.7%</td></tr>
  <tr align="center"><th rowspan="2">0917</th><td>플래티넘 ↑</td><td>88.4%</td><td>93.4%</td></tr>
  <tr align="center"><td>전체</td><td>86.2%</td><td>92.9%</td></tr>
</table>
플래티넘 이상 4.5만건
데이터 전체 20만건

<!--   ### 3.3 소결
* <b>성능에 대한 의미</b><br>
왜 잘 나오는지
이 두 가지 방법을 사용하여 모델의 성능을 비교하였다. 이를 통해 각 방법의 장단점을 파앙ㄱ하고

* <b>핵심 데이터 항목에 대한 추정 및 분석<b><br>
  프로젝트에서 주요하게 다뤘던 데이터 항목들은 소환사 정보, 챔피언 정보, 게임 정보, 랭킹 및 리그 정보 등이었다. 이러한 항목들을 통해 모델은 플레이어의 경험, 챔피언의 능력, 게임의 진행 상황, 플레이어의 순위 등을 파악하여 예측을 수행했다.

특히, 소환사의 행동 패턴, 특정 챔피언의 픽률 및 밴률, 게임의 초반과 후반에 따른 데이터의 중요성을 도출했다. 이를 통해 게임에서 승리하는 데 영향을 미치는 핵심적인 변수들을 확인하고 모델의 학습에 활용했습니다.

이러한 데이터 항목들의 추정과 분석을 통해 게임의 다양한 측면을 이해하고, 모델의 예측력을 개선하는 데 기여했습니다. 추후 프로젝트나 유사한 분야에서의 활용을 위해 이러한 데이터의 중요성과 영향을 보다 정교하게 이해할 수 있게 되었습니다. -->

<hr>

## 4. 결론 및 배운점

프로젝트를 통해 다량의 League of Legends 게임 데이터를 분석하고, 승패를 예측하는 모델을 개발하는 과정에서 데이터 과학 및 머신러닝 기술에 대한 이해와 경험이 증가했다.

LoL의 다양한 측면에 대한 데이터 분석을 통해 게임의 전략, 팀워크, 챔피언 간의 상호작용 등에 대한 깊은 이해를 얻었다. 이를 통해 게임의 복잡성을 이해하고, 플레이어들 간의 경쟁에서 중요한 영향을 미치는 요소들을 파악할 수 있었다.

Riot Games API를 사용하여 게임 데이터를 수집하는 과정을 배웠고, 해당 데이터를 활용해 분석하는 경험을 쌓았다. API를 통한 데이터 획득, 전처리, 모델 학습 등의 과정을 이해하고 활용할 수 있게 된 것이 중요한 점 중 하나이다.

개발한 승패 예측 모델의 성능을 평가하고, 모델의 강점과 약점을 파악하며 모델을 향상시키는 데 필요한 통계적 평가 기술에 대한 이해가 높아졌다.

<hr>
       
       
   ## References
   [01] https://weekly.chosun.com/news/articleView.html?idxno=30406 <br>
   [02] https://www.thelog.co.kr/report/reportView.do?nSeq=265 <br>
   [03] https://pgr21.com/free2/72613 <br>
   [04] https://developer.riotgames.com/

   




