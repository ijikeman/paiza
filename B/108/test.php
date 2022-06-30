<?php
    $fp = @fopen('./test.txt', 'r');
    list($MAX_GONDRA, $MAX_GROUP) = explode(' ', trim(fgets($fp, 4096)));
    $GONDRA_LIST = array();
    $MEMBER_LIST = array();
    $BOADING_LIST = array(); // 各ゴンドラ毎に乗った人数を加算

    $index=0;
    while (($line = fgets($fp, 4096)) !== false ) {
        // ゴンドラ乗れる人数リスト
        if ($index < $MAX_GONDRA) {
            array_push($GONDRA_LIST, $line);
        } else {
            // グループの人数リスト
            array_push($MEMBER_LIST, $line);
        }
        $index++;
    }

    /* debug
    print_r($GONDRA_LIST);
    print_r($MEMBER_LIST);
    */

    // ゴンドラ番号
    $gondra_index = 0;
    $max_board_num = 0;

    // 次のゴンドラ乗車人数を取得
    while($max_board_num = array_slice($GONDRA_LIST, $gondra_index, 1)) {
        // 乗車グループがなくなれば終了
        if (count($MEMBER_LIST) == 0) {
            break;
        } else {
            // グループ１つずつ処理
            $member = array_shift($MEMBER_LIST);
        }

        // ゴンドラに乗れる人数がグループ人数より少ない場合は、全員乗れない
        if ($member > $max_board_num) {
            $amari = $member - $max_board_num;
            $BOADING_LIST[$i]+=$max_board_num; // 乗車記録に最大人数を記録
        }
        $gondra_index++; // 次のゴンドラに移る
    }
?>
