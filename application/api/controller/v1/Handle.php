<?php

namespace app\api\controller\v1;

use think\Controller;
use think\Request;
use app\api\common\Common;
use app\api\controller\Send;
use app\api\controller\Api;
use app\api\model\UsersModel;
use app\api\validate\SignInValidate;

class Handle extends Api {
    
    use Send;

    /**
    * 注册验证
    */
    public function register(Request $request) {
        Common::valid(new SignInValidate);
        $account = UsersModel::where(['email'=>$request->post("email")])->find();
        if (!empty($account)) {
            self::returnMsg(500, '账户已存在', ['code'=>101]);
        } else {
            $user = new UsersModel;
            $user->save([
                'email'     =>  $request->post("email"),
                'password'  =>  md5(md5($request->post('password')).'RSSS_READER')
            ]);
            self::returnMsg(200, '注册完成', ['code'=>200, 'email'=>$request->post("email"), 'user_id'=>$user['id']]);
        }
    }

    /**
    * 登入验证
    */
    public function signIn(Request $request) {
        Common::valid(new SignInValidate);
        $account = UsersModel::where(['email'=>$request->post("email")])->find();
        if (!empty($account)) {
            if (md5(md5($request->post('password')).'RSSS_READER') == $account['password']) {
                self::returnMsg(200, '信息验证有效', ['email'=>$account['email'], 'user_id'=>$account['id']]);
            } else {
                self::returnMsg(500, '信息验证无效', ['code'=>102]);
            }
        } else {
            self::returnMsg(500, '账户不存在', ['code'=>103]);
        }
    }

    /**
    * 添加一条订阅
    */
    public function addRSS(Request $request) {
        
    }

    public function getNews(Request $request) {

    }

}
