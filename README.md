# MariaDB에 저장될 정보들

## USER_INFO
+ id
+ name
+ password
+ nickname
+ character ( ,를 사용하여 캐릭터 닉네임을 구분한다.)
+ guild
+ select_character

## USER_CHARACTER
+ id
+ owner
+ name
+ skin
+ rank
+ exp
+ weapon('id'값으로 저장됨)


# 파일로 저장될 정보들
json 형태로 저장될 예정

+ 인벤토리

    파일 이름은 유저ID로 저장

    + './UserData/Inventory'에 현json파일로 저장됨
    + wand
        + 'id' : 0 (아이템의 고유 key값)
        + 'character' : 'name' (누가꼈는지확인, 없으면 null)
    + consume
    + material
+ 퀘스트진행사항 
        
    파일 이름은 유저ID로 저장

    + './UserData/Quest'에 현 json파일로 저장됨
        + 진행사항이 True, False로 구분됨

+ 정령가방

    파일 이름은 유저 ID로 저장

    + './UserData/soul'에 현 json파일로 저장됨
    + 정보(그 이외 정보는 Data폴더에 저장됨)
        + id
        + name
        + exp

+ 탈것들

    파일 이름은 유저 ID로 저장

    + './rider'에 현 json파일로 저장됨
    + 정보(그 이외 정보는 Data폴더에 저장됨)
        + id
        + name
        + nickname
        + exp

# 유저 데이터 구성